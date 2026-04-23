# Training Report

**Date**: 2026-03-04 00:52:40

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/original |
| Device | cuda |

## Training Results

- **Training Time**: 295.5 minutes
- **Best Epoch**: 26/27
- **Best Validation Loss**: 153.0225
- **Best Validation RMSE**: 12.3702 W/m²
- **Peak GPU Memory (VRAM)**: 20620.22 MB

## Test Results

- **MSE Loss**: 130.3214
- **RMSE**: 11.4158 W/m²
- **MAE**: 6.9135 W/m²
- **R² Score**: 0.9982

## Generated Files

- Model checkpoint: `fisheye_model_2026-03-03_19-56.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
