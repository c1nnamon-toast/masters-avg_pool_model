# Training Report

**Date**: 2026-03-24 20:33:49

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 15 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_rubsheet_square |
| Device | cuda |

## Training Results

- **Training Time**: 39.8 minutes
- **Best Epoch**: 15/15
- **Best Validation Loss**: 365.3900
- **Best Validation RMSE**: 19.1152 W/m²
- **Peak GPU Memory (VRAM)**: 5119.57 MB

## Test Results

- **MSE Loss**: 307.5448
- **RMSE**: 17.5370 W/m²
- **MAE**: 10.7541 W/m²
- **R² Score**: 0.9959

## Generated Files

- Model checkpoint: `rubsheet_square_model_gap_2026-03-24_19-53.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
