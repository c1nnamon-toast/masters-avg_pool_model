import torch
import torch.nn.functional as F
import numpy as np
import cv2

class RegressionGradCAM:
    """
    Grad-CAM implementation specifically for Regression tasks.
    Instead of backpropagating a class score, we backpropagate the predicted scalar value.
    """
    def __init__(self, model, target_layer):
        self.model = model
        self.model.eval()
        self.target_layer = target_layer
        self.gradients = None
        self.activations = None

        # Hook to save gradients and activations
        self.target_layer.register_forward_hook(self.save_activation)
        self.target_layer.register_full_backward_hook(self.save_gradient)

    def save_activation(self, module, input, output):
        self.activations = output

    def save_gradient(self, module, grad_input, grad_output):
        # Gradients are stored as a tuple, we need the first element
        self.gradients = grad_output[0]

    def __call__(self, input_tensor):
        """
        Args:
            input_tensor: (1, C, H, W) torch tensor
        Returns:
            heatmap: np.array of shape (H, W)
            prediction: float
        """
        # 1. Forward pass
        output = self.model(input_tensor)
        prediction = output.item()

        # 2. Backward pass
        # We backpropagate the output value itself. 
        # This highlights regions contributing to the magnitude of the prediction.
        self.model.zero_grad()
        output.backward()

        # 3. Get captured gradients and activations
        gradients = self.gradients.cpu().data.numpy()[0] # (Channels, H, W)
        activations = self.activations.cpu().data.numpy()[0] # (Channels, H, W)

        # 4. Global Average Pooling of gradients to get neuron importance weights
        weights = np.mean(gradients, axis=(1, 2)) # (Channels,)

        # 5. Weighted combination of feature maps
        # Multiply each feature map by its weight
        cam = np.zeros(activations.shape[1:], dtype=np.float32)
        for i, w in enumerate(weights):
            cam += w * activations[i]

        # 6. Apply ReLU (we only care about positive influence)
        cam = np.maximum(cam, 0)

        # 7. Resize heatmap to input image size
        img_h, img_w = input_tensor.shape[2], input_tensor.shape[3]
        cam = cv2.resize(cam, (img_w, img_h))

        # 8. Normalize between 0 and 1
        if np.max(cam) != 0:
            cam = cam - np.min(cam)
            cam = cam / np.max(cam)
        
        return cam, prediction

def overlay_heatmap(img_tensor, heatmap, alpha=0.55,
                    normalize_mean=None, normalize_std=None):
    """
    Denormalize the image tensor (if needed) and create a red-tint overlay.

    The overlay uses pure red with per-pixel opacity proportional to the
    heatmap intensity: transparent where there is no contribution,
    saturated red where the model focused most.

    Parameters
    ----------
    normalize_mean, normalize_std : list of 3 floats or None
        If the dataloader applied transforms.Normalize with these values,
        pass them here so the original pixel colours are recovered.

    Returns
    -------
    original : np.ndarray, uint8, RGB, (H, W, 3)
    overlay  : np.ndarray, uint8, RGB, (H, W, 3)
    """
    img = img_tensor.cpu().numpy()[0].transpose(1, 2, 0)  # (H, W, C) RGB float

    # Reverse normalization: original = img * std + mean
    if normalize_mean is not None and normalize_std is not None:
        std = np.asarray(normalize_std, dtype=np.float32)
        mean = np.asarray(normalize_mean, dtype=np.float32)
        img = img * std + mean

    img = np.clip(img, 0, 1)

    # Overlay: pure red tint with per-pixel alpha scaled by heatmap value
    red = np.array([1.0, 0.0, 0.0], dtype=np.float32)
    alpha_map = (heatmap * alpha)[:, :, np.newaxis]  # (H, W, 1)
    blended = (1.0 - alpha_map) * img + alpha_map * red
    blended = np.clip(blended, 0, 1)

    return np.uint8(255 * img), np.uint8(255 * blended)