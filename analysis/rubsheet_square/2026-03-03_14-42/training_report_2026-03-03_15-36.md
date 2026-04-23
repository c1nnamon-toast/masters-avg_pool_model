# Training Report

**Date**: 2026-03-03 15:36:52

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 20 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_rubsheet_square |
| Device | cuda |

## Training Results

- **Training Time**: 53.8 minutes
- **Best Epoch**: 19/20
- **Best Validation Loss**: 166.1490
- **Best Validation RMSE**: 12.8899 W/m²
- **Peak GPU Memory (VRAM)**: 5320.09 MB

## Test Results

- **MSE Loss**: 145.0263
- **RMSE**: 12.0427 W/m²
- **MAE**: 7.1474 W/m²
- **R² Score**: 0.9980

## Generated Files

- Model checkpoint: `rubsheet_square_model_2026-03-03_14-42.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
