# Training Report

**Date**: 2026-03-03 02:35:36

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 20 |
| Dataset | /home/xtsimbota_135764/masters/dataset/original |
| Device | cuda |

## Training Results

- **Training Time**: 219.0 minutes
- **Best Epoch**: 18/20
- **Best Validation Loss**: 204.1561
- **Best Validation RMSE**: 14.2883 W/m²
- **Peak GPU Memory (VRAM)**: 20620.22 MB

## Test Results

- **MSE Loss**: 195.0440
- **RMSE**: 13.9658 W/m²
- **MAE**: 8.3439 W/m²
- **R² Score**: 0.9974

## Generated Files

- Model checkpoint: `fisheye_model_2026-03-02_22-55.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
