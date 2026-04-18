# Training Report

**Date**: 2026-03-24 17:50:01

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 15 |
| Dataset | /home/xtsimbota_135764/masters/dataset/original |
| Device | cuda |

## Training Results

- **Training Time**: 163.8 minutes
- **Best Epoch**: 12/15
- **Best Validation Loss**: 528.5108
- **Best Validation RMSE**: 22.9894 W/m²
- **Peak GPU Memory (VRAM)**: 20420.05 MB

## Test Results

- **MSE Loss**: 499.3603
- **RMSE**: 22.3464 W/m²
- **MAE**: 13.7137 W/m²
- **R² Score**: 0.9933

## Generated Files

- Model checkpoint: `fisheye_model_gap_2026-03-24_15-05.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
