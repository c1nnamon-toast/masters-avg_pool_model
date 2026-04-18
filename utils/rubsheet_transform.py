import numpy as np
import cv2

def build_rubbersheet_map(center, radius, target_size):
    """
    Builds the mapping for Polar to Cartesian transformation (Circle -> Rect).
    """
    target_w, target_h = target_size
    ys, xs = np.indices((target_h, target_w))
    
    # y -> radius, x -> angle
    r_normalized = ys / float(target_h - 1)
    r = r_normalized * radius
    theta = (xs / float(target_w)) * 2 * np.pi
    
    src_x = center[0] + r * np.cos(theta)
    src_y = center[1] + r * np.sin(theta)
    
    return src_x.astype(np.float32), src_y.astype(np.float32)

def build_inverse_rubbersheet_map(center, radius, target_size, source_rect_size):
    """
    Builds the mapping for Cartesian to Polar transformation (Rect -> Circle).
    Used to project the rectangular heatmap back onto the circular image.
    
    Args:
        center: (cx, cy) of the output circle
        radius: Radius of the output circle
        target_size: (width, height) of the output circular image
        source_rect_size: (width, height) of the input rectangular image
    """
    target_w, target_h = target_size
    rect_w, rect_h = source_rect_size
    
    # Create grid for the circular output
    ys, xs = np.indices((target_h, target_w))
    
    # Calculate R and Theta for every pixel in the output circle
    # We shift xs, ys relative to center
    y_shifted = ys - center[1]
    x_shifted = xs - center[0]
    
    r = np.sqrt(x_shifted**2 + y_shifted**2)
    theta = np.arctan2(y_shifted, x_shifted) # Returns -pi to pi
    
    # Normalize theta to 0 -> 1 (corresponding to 0 -> 2pi)
    # arctan2 returns angle in range [-pi, pi].
    # We need to map this to match the unwrapping logic:
    # In unwrap: x=0 is theta=0. x=width is theta=2pi.
    # Note: We must ensure the direction matches (CW vs CCW and starting point).
    # Usually arctan2 is CCW from x-axis. 
    # If your unwrap logic was standard, we just normalize:
    theta = np.where(theta < 0, theta + 2*np.pi, theta)
    
    # Map R (0 to radius) -> Rect Y (0 to rect_h)
    # Map Theta (0 to 2pi) -> Rect X (0 to rect_w)
    
    map_x = (theta / (2 * np.pi)) * rect_w
    map_y = (r / radius) * rect_h
    
    # Mask out pixels outside the radius
    mask = r > radius
    
    # We can handle the mask later or let remap handle it (it usually repeats edges or black)
    # We'll set the map to -1 for out of bounds so opencv handles it gracefully if using border constant
    
    return map_x.astype(np.float32), map_y.astype(np.float32), mask

def unwrap_image(img, map_x, map_y):
    """Apply the unwrap transformation."""
    return cv2.remap(img, map_x, map_y, interpolation=cv2.INTER_LINEAR)

def rewrap_image(rect_img, map_x, map_y):
    """Apply the inverse transformation (rewrap)."""
    return cv2.remap(rect_img, map_x, map_y, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)