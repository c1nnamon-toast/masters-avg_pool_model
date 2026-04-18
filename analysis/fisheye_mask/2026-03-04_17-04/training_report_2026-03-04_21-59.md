# Training Report

**Date**: 2026-03-04 21:59:11

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_mask |
| Device | cuda |

## Training Results

- **Training Time**: 294.0 minutes
- **Best Epoch**: 23/27
- **Best Validation Loss**: 404.7202
- **Best Validation RMSE**: 20.1177 W/m²
- **Peak GPU Memory (VRAM)**: 20620.22 MB

## Test Results

- **MSE Loss**: 379.4505
- **RMSE**: 19.4795 W/m²
- **MAE**: 11.2197 W/m²
- **R² Score**: 0.9949

## Generated Files

- Model checkpoint: `fisheye_mask_model_2026-03-04_17-04.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
