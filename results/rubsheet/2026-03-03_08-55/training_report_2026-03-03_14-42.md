# Training Report

**Date**: 2026-03-03 14:42:51

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 8 |
| Epochs | 20 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_rubsheet |
| Device | cuda |

## Training Results

- **Training Time**: 346.4 minutes
- **Best Epoch**: 18/20
- **Best Validation Loss**: 245.8453
- **Best Validation RMSE**: 15.6795 W/m²
- **Peak GPU Memory (VRAM)**: 16229.50 MB

## Test Results

- **MSE Loss**: 234.2225
- **RMSE**: 15.3043 W/m²
- **MAE**: 9.1774 W/m²
- **R² Score**: 0.9968

## Generated Files

- Model checkpoint: `rubsheet_model_2026-03-03_08-55.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
