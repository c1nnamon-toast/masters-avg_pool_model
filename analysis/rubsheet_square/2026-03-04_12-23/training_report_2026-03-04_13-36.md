# Training Report

**Date**: 2026-03-04 13:36:41

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_rubsheet_square |
| Device | cuda |

## Training Results

- **Training Time**: 72.7 minutes
- **Best Epoch**: 25/27
- **Best Validation Loss**: 139.8967
- **Best Validation RMSE**: 11.8278 W/m²
- **Peak GPU Memory (VRAM)**: 5320.09 MB

## Test Results

- **MSE Loss**: 118.9924
- **RMSE**: 10.9084 W/m²
- **MAE**: 6.5774 W/m²
- **R² Score**: 0.9984

## Generated Files

- Model checkpoint: `rubsheet_square_model_2026-03-04_12-23.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
