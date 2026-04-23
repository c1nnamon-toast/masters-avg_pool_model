# Training Report

**Date**: 2026-03-03 08:55:09

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 20 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_mask_crop |
| Device | cuda |

## Training Results

- **Training Time**: 160.1 minutes
- **Best Epoch**: 19/20
- **Best Validation Loss**: 523.0716
- **Best Validation RMSE**: 22.8708 W/m²
- **Peak GPU Memory (VRAM)**: 15068.03 MB

## Test Results

- **MSE Loss**: 521.0597
- **RMSE**: 22.8267 W/m²
- **MAE**: 14.0045 W/m²
- **R² Score**: 0.9930

## Generated Files

- Model checkpoint: `fisheye_mask_crop_model_2026-03-03_06-14.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
