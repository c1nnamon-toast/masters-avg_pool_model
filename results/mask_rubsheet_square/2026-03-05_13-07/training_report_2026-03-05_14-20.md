# Training Report

**Date**: 2026-03-05 14:20:08

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_mask_rubsheet_square |
| Device | cuda |

## Training Results

- **Training Time**: 72.6 minutes
- **Best Epoch**: 26/27
- **Best Validation Loss**: 375.1982
- **Best Validation RMSE**: 19.3700 W/m²
- **Peak GPU Memory (VRAM)**: 5320.09 MB

## Test Results

- **MSE Loss**: 327.3214
- **RMSE**: 18.0920 W/m²
- **MAE**: 10.1925 W/m²
- **R² Score**: 0.9956

## Generated Files

- Model checkpoint: `mask_rubsheet_square_model_2026-03-05_13-07.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
