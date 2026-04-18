"""
Grad-CAM visualization for the rubsheet experiment.
Loads the trained rubsheet model, runs inference on the test set,
selects the 10 best and 10 worst predictions, and generates
Grad-CAM heatmap grids for each group.

Note: rubbersheet images are wide panoramic strips (3355x534).
The grid layout is adapted for this aspect ratio.
"""
import sys
import os
import glob
import re

EXPERIMENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(EXPERIMENT_DIR))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, EXPERIMENT_DIR)

import torch
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable
import logging
from tqdm import tqdm

import config_rubsheet as config
from nn.model import SkyCNN
from nn.loader import get_dataloaders
from utils.cgradcam import RegressionGradCAM, overlay_heatmap
from logger_helper import logger_setup

logger = logging.getLogger(__name__)


def find_latest_model(base_path):
    """
    Find the latest model file based on timestamp suffix.
    Model files are named like: rubsheet_model_2026-03-04_00-52.pth
    """
    model_dir = os.path.dirname(base_path)
    base_name = os.path.basename(base_path).replace('.pth', '')
    
    pattern = os.path.join(model_dir, f"{base_name}_*.pth")
    model_files = glob.glob(pattern)
    
    if not model_files:
        if os.path.exists(base_path):
            return base_path
        raise FileNotFoundError(f"No model files found matching {pattern}")
    
    def extract_timestamp(path):
        match = re.search(r'(\d{4}-\d{2}-\d{2}_\d{2}-\d{2})\.pth$', path)
        return match.group(1) if match else ''
    
    model_files.sort(key=extract_timestamp, reverse=True)
    return model_files[0]


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


def plot_gradcam_grid(cases, cam_obj, device, title_prefix, save_path):
    """
    For each case, plot three rows stacked vertically:
      Row A – Original Input Image:              the unmodified sky strip.
      Row B – Pixel Contribution Map (Grad-CAM): which regions the model
              relied on most (deeper red = higher contribution, white = none).
      Row C – Contribution Applied to Original:  a red tint blended onto the
              original so you can see which sky features drove the prediction.
    Because rubbersheet images are very wide (6:1 aspect), we stack vertically.
    """
    n = len(cases)
    # Each image gets 3 sub-rows; use generous height for wide strips
    fig, axes = plt.subplots(n * 3, 1, figsize=(22, 3.0 * n * 3 + 1.5))

    logger.info(f"Generating Grad-CAM grid: {title_prefix} ({n} images)...")

    for i, case in enumerate(cases):
        img_tensor = case["image"].to(device)

        with torch.enable_grad():
            heatmap, pred = cam_obj(img_tensor)

        orig_img, overlay = overlay_heatmap(
            img_tensor, heatmap,
            normalize_mean=config.NORMALIZE_MEAN,
            normalize_std=config.NORMALIZE_STD,
        )

        row_base = i * 3

        # Row A – Original Input Image
        axes[row_base].imshow(orig_img)
        axes[row_base].set_title(
            f"#{i+1}  Original Input Image  |  True: {case['label']:.0f} W/m²  |  "
            f"Pred: {case['prediction']:.0f} W/m²  |  Err: {case['error']:.1f}",
            fontsize=11, loc="left",
        )
        axes[row_base].axis("off")

        # Row B – Pixel Contribution Map
        axes[row_base + 1].imshow(heatmap, cmap="Reds", vmin=0, vmax=1)
        axes[row_base + 1].set_title(
            "Pixel Contribution Map (Grad-CAM) — more intense red = higher contribution",
            fontsize=9, loc="left",
        )
        axes[row_base + 1].axis("off")

        # Row C – Contribution Applied to Original
        axes[row_base + 2].imshow(overlay)
        axes[row_base + 2].set_title(
            "Contribution Applied to Original",
            fontsize=9, loc="left",
        )
        axes[row_base + 2].axis("off")

    # ── Colorbar legend ─────────────────────────────────────────────
    cbar_ax = fig.add_axes([0.15, 0.008, 0.7, 0.006])
    norm = mcolors.Normalize(vmin=0, vmax=1)
    sm = ScalarMappable(cmap="Reds", norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, cax=cbar_ax, orientation="horizontal")
    cbar.set_ticks([0, 0.5, 1])
    cbar.set_ticklabels(["No contribution", "Medium", "High contribution"])
    cbar.ax.tick_params(labelsize=9)

    # ── Descriptive caption ─────────────────────────────────────────
    caption = (
        "Row A: The original sky strip fed to the model.  "
        "Row B: Pixel contribution map — the more intense the red, "
        "the more that region contributed to the predicted irradiance.  "
        "Row C: Contribution overlaid on the original, revealing which sky features "
        "(e.g. sun position, cloud edges) drove the prediction."
    )
    fig.text(0.5, 0.002, caption, ha="center", fontsize=8, style="italic",
             wrap=True, color="0.3")

    plt.suptitle(f"{title_prefix}  (Regression Grad-CAM — Rubsheet)", fontsize=16, y=1.0)
    plt.tight_layout(rect=[0, 0.02, 1, 0.98])
    plt.savefig(save_path, dpi=200, bbox_inches="tight")
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
        normalize_mean=config.NORMALIZE_MEAN,
        normalize_std=config.NORMALIZE_STD,
    )

    # ── Load trained model ──────────────────────────────────────────
    model_path = find_latest_model(config.MODEL_SAVE_PATH)
    logger.info(f"Loading model from {model_path}")
    model = SkyCNN().to(device)
    model.load_state_dict(
        torch.load(model_path, map_location=device, weights_only=True)
    )

    # ── Grad-CAM targeting the last conv block ──────────────────────
    grad_cam = RegressionGradCAM(model, model.conv_block4)

    # ── Select best/worst ───────────────────────────────────────────
    best_cases, worst_cases = select_test_cases(model, test_loader, device, n=10)

    # ── Output directory ────────────────────────────────────────────
    output_dir = os.path.join(config.ANALYSIS_DIR, "gradcam")
    os.makedirs(output_dir, exist_ok=True)

    plot_gradcam_grid(
        best_cases, grad_cam, device,
        "Top 10 Best Predictions",
        os.path.join(output_dir, "best_10_gradcam.png"),
    )
    plot_gradcam_grid(
        worst_cases, grad_cam, device,
        "Top 10 Worst Predictions",
        os.path.join(output_dir, "worst_10_gradcam.png"),
    )

    logger.info("Grad-CAM visualisation complete.")


if __name__ == "__main__":
    main()
