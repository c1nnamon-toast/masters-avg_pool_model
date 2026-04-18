# Training Report

**Date**: 2026-03-06 19:06:30

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_rubsheet_2to1 |
| Device | cuda |

## Training Results

- **Training Time**: 145.3 minutes
- **Best Epoch**: 24/27
- **Best Validation Loss**: 164.5606
- **Best Validation RMSE**: 12.8281 W/m²
- **Peak GPU Memory (VRAM)**: 10421.30 MB

## Test Results

- **MSE Loss**: 134.7042
- **RMSE**: 11.6062 W/m²
- **MAE**: 6.7827 W/m²
- **R² Score**: 0.9982

## Generated Files

- Model checkpoint: `rubsheet_2to1_model_2026-03-06_16-40.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
