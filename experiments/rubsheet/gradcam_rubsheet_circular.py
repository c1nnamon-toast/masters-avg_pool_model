"""
Circular Grad-CAM visualization for the rubsheet experiment.
Loads the trained rubsheet model, generates Grad-CAM on the rectangular
panoramic strips, then warps both heatmap and overlay back to the
original circular fisheye view using the inverse rubbersheet transform.
"""
import sys
import os

EXPERIMENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(EXPERIMENT_DIR))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, EXPERIMENT_DIR)

import torch
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable
import logging
from tqdm import tqdm

import config_rubsheet as config
from nn.model import SkyCNN
from nn.loader import get_dataloaders
from utils.cgradcam import RegressionGradCAM, overlay_heatmap
from utils.rubsheet_transform import build_inverse_rubbersheet_map, rewrap_image
from logger_helper import logger_setup

logger = logging.getLogger(__name__)

# Original fisheye image geometry
ORIG_CENTER = (534, 534)
ORIG_RADIUS = 534
ORIG_SIZE = (1068, 1068)  # (width, height)


def select_test_cases(model, dataloader, device, n=10):
    """
    Run inference on the full test set and return the n best and n worst
    predictions ranked by absolute error.
    """
    model.eval()
    results = []

    logger.info("Running inference on test set...")
    with torch.no_grad():
        for images, labels in tqdm(dataloader, desc="Scanning test set"):
            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)

            for j in range(images.size(0)):
                results.append({
                    "image": images[j].unsqueeze(0).cpu(),
                    "label": labels[j].item(),
                    "prediction": outputs[j].item(),
                    "error": abs(outputs[j].item() - labels[j].item()),
                })

    results.sort(key=lambda x: x["error"])

    best = results[:n]
    worst = results[-n:]
    worst.reverse()

    logger.info(f"Best error range : {best[0]['error']:.2f} – {best[-1]['error']:.2f}")
    logger.info(f"Worst error range: {worst[0]['error']:.2f} – {worst[-1]['error']:.2f}")

    return best, worst


def warp_to_circular(rect_img_bgr, inv_map_x, inv_map_y, mask):
    """
    Warp a rectangular (panoramic) image back to circular fisheye view.
    Pixels outside the circle radius are set to black.
    """
    circular = rewrap_image(rect_img_bgr, inv_map_x, inv_map_y)
    circular[mask] = 0
    return circular


def plot_circular_gradcam_grid(cases, cam_obj, device, inv_map_x, inv_map_y,
                                circle_mask, title_prefix, save_path):
    """
    For each case, 3 columns (all warped back to circular fisheye view):
      Col 1 – Original Input Image:              the sky image reconstructed
              from the rubsheet strip back into the circular fisheye view.
      Col 2 – Pixel Contribution Map (Grad-CAM): which regions the model
              relied on most (deeper red = higher contribution, white = none).
      Col 3 – Contribution Applied to Original:  a red tint blended onto
              the original so you can see exactly which sky features
              drove the prediction.
    Plus a colorbar at the bottom.
    """
    n = len(cases)
    fig, axes = plt.subplots(n, 3, figsize=(15, 4.5 * n + 1.5))
    if n == 1:
        axes = np.expand_dims(axes, 0)

    # Column headers (only on the first row)
    col_headers = [
        "Original Input Image",
        "Pixel Contribution Map (Grad-CAM)",
        "Contribution Applied to Original",
    ]

    logger.info(f"Generating circular Grad-CAM grid: {title_prefix} ({n} images)...")

    for i, case in enumerate(cases):
        img_tensor = case["image"].to(device)

        with torch.enable_grad():
            heatmap, pred = cam_obj(img_tensor)

        orig_img, overlay = overlay_heatmap(
            img_tensor, heatmap,
            normalize_mean=config.NORMALIZE_MEAN,
            normalize_std=config.NORMALIZE_STD,
        )

        # ── Warp rectangular results back to circular ───────────────
        # overlay_heatmap now returns RGB uint8 — warp directly
        circ_orig = warp_to_circular(orig_img, inv_map_x, inv_map_y, circle_mask)
        circ_overlay = warp_to_circular(overlay, inv_map_x, inv_map_y, circle_mask)

        heatmap_u8 = np.uint8(255 * heatmap)
        circ_heatmap_u8 = rewrap_image(heatmap_u8, inv_map_x, inv_map_y)
        circ_heatmap_u8[circle_mask] = 0
        circ_heatmap_float = circ_heatmap_u8.astype(np.float32) / 255.0

        # ── Plot ────────────────────────────────────────────────────
        # Col 1 – Original
        label_text = f"True: {case['label']:.0f} W/m²  |  Pred: {case['prediction']:.0f} W/m²"
        if i == 0:
            axes[i, 0].set_title(f"{col_headers[0]}\n{label_text}", fontsize=10)
        else:
            axes[i, 0].set_title(label_text, fontsize=10)
        axes[i, 0].imshow(circ_orig)
        axes[i, 0].axis("off")

        # Col 2 – Pixel Contribution Map
        axes[i, 1].imshow(circ_heatmap_float, cmap="Reds", vmin=0, vmax=1)
        if i == 0:
            axes[i, 1].set_title(col_headers[1], fontsize=10)
        axes[i, 1].axis("off")

        # Col 3 – Contribution Applied to Original
        axes[i, 2].imshow(circ_overlay)
        if i == 0:
            axes[i, 2].set_title(f"{col_headers[2]}\nAbs Error: {case['error']:.1f}", fontsize=10)
        else:
            axes[i, 2].set_title(f"Abs Error: {case['error']:.1f}", fontsize=10)
        axes[i, 2].axis("off")

    # ── Colorbar legend ─────────────────────────────────────────────
    cbar_ax = fig.add_axes([0.15, 0.025, 0.7, 0.012])
    norm = mcolors.Normalize(vmin=0, vmax=1)
    sm = ScalarMappable(cmap="Reds", norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, cax=cbar_ax, orientation="horizontal")
    cbar.set_ticks([0, 0.5, 1])
    cbar.set_ticklabels(["No contribution", "Medium", "High contribution"])
    cbar.ax.tick_params(labelsize=9)

    # ── Descriptive caption ─────────────────────────────────────────
    caption = (
        "Col 1: The original sky image (warped back from rubsheet strip to circular fisheye view).  "
        "Col 2: Pixel contribution map — the more intense the red, "
        "the more that region contributed to the predicted irradiance.  "
        "Col 3: Contribution overlaid on the original, revealing which sky features "
        "(e.g. sun position, cloud edges) drove the prediction."
    )
    fig.text(0.5, 0.005, caption, ha="center", fontsize=8, style="italic",
             wrap=True, color="0.3")

    plt.suptitle(
        f"{title_prefix}  (Regression Grad-CAM — Rubsheet → Circular)",
        fontsize=16,
    )
    plt.tight_layout(rect=[0, 0.05, 1, 0.97])
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    logger.info(f"Saved → {save_path}")


def main():
    logger_setup(experiment_logfile=config.LOG_FILE)
    device = config.DEVICE

    # ── Load test data ──────────────────────────────────────────────
    logger.info("Loading test data...")
    _, _, test_loader, _ = get_dataloaders(
        train_csv=config.TRAIN_CSV,
        val_csv=config.VAL_CSV,
        test_csv=config.TEST_CSV,
        train_image_dir=config.TRAIN_IMAGE_DIR,
        val_image_dir=config.VAL_IMAGE_DIR,
        test_image_dir=config.TEST_IMAGE_DIR,
        batch_size=config.BATCH_SIZE,
        num_workers=config.NUM_WORKERS,
        pin_memory=config.PIN_MEMORY,
        border_crop=None,
        augment_train=False,
        normalize_mean=config.NORMALIZE_MEAN,
        normalize_std=config.NORMALIZE_STD,
    )

    # ── Load trained model ──────────────────────────────────────────
    logger.info(f"Loading model from {config.MODEL_SAVE_PATH}")
    model = SkyCNN().to(device)
    model.load_state_dict(
        torch.load(config.MODEL_SAVE_PATH, map_location=device, weights_only=True)
    )

    # ── Grad-CAM targeting the last conv block ──────────────────────
    grad_cam = RegressionGradCAM(model, model.conv_block4)

    # ── Build inverse rubbersheet mapping ───────────────────────────
    # Rubsheet images are loaded at their native resolution by the dataloader.
    # We need to figure out the actual rect size from a sample.
    sample_batch = next(iter(test_loader))
    rect_h, rect_w = sample_batch[0].shape[2], sample_batch[0].shape[3]
    logger.info(f"Rubsheet tensor size: {rect_w}×{rect_h}")

    inv_map_x, inv_map_y, circle_mask = build_inverse_rubbersheet_map(
        center=ORIG_CENTER,
        radius=ORIG_RADIUS,
        target_size=ORIG_SIZE,
        source_rect_size=(rect_w, rect_h),
    )
    logger.info("Inverse rubbersheet map built.")

    # ── Select best/worst ───────────────────────────────────────────
    best_cases, worst_cases = select_test_cases(model, test_loader, device, n=10)

    # ── Output directory ────────────────────────────────────────────
    output_dir = os.path.join(config.ANALYSIS_DIR, "gradcam_circular")
    os.makedirs(output_dir, exist_ok=True)

    plot_circular_gradcam_grid(
        best_cases, grad_cam, device, inv_map_x, inv_map_y, circle_mask,
        "Top 10 Best Predictions",
        os.path.join(output_dir, "best_10_gradcam_circular.png"),
    )
    plot_circular_gradcam_grid(
        worst_cases, grad_cam, device, inv_map_x, inv_map_y, circle_mask,
        "Top 10 Worst Predictions",
        os.path.join(output_dir, "worst_10_gradcam_circular.png"),
    )

    logger.info("Circular Grad-CAM visualisation complete.")


if __name__ == "__main__":
    main()
