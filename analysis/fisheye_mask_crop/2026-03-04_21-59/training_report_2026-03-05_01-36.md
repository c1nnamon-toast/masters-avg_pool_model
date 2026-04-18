# Training Report

**Date**: 2026-03-05 01:36:11

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_mask_crop |
| Device | cuda |

## Training Results

- **Training Time**: 216.4 minutes
- **Best Epoch**: 25/27
- **Best Validation Loss**: 409.2441
- **Best Validation RMSE**: 20.2298 W/m²
- **Peak GPU Memory (VRAM)**: 15068.03 MB

## Test Results

- **MSE Loss**: 379.7266
- **RMSE**: 19.4866 W/m²
- **MAE**: 10.8239 W/m²
- **R² Score**: 0.9949

## Generated Files

- Model checkpoint: `fisheye_mask_crop_model_2026-03-04_21-59.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
