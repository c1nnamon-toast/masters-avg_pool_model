# Training Report

**Date**: 2026-03-03 06:14:27

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 20 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_mask |
| Device | cuda |

## Training Results

- **Training Time**: 218.1 minutes
- **Best Epoch**: 20/20
- **Best Validation Loss**: 544.2111
- **Best Validation RMSE**: 23.3283 W/m²
- **Peak GPU Memory (VRAM)**: 20620.19 MB

## Test Results

- **MSE Loss**: 507.2960
- **RMSE**: 22.5232 W/m²
- **MAE**: 14.8208 W/m²
- **R² Score**: 0.9932

## Generated Files

- Model checkpoint: `fisheye_mask_model_2026-03-03_02-35.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
