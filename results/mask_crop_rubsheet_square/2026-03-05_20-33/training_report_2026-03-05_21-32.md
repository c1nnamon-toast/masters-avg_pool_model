# Training Report

**Date**: 2026-03-05 21:32:14

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_mask_crop_rubsheet_square |
| Device | cuda |

## Training Results

- **Training Time**: 58.8 minutes
- **Best Epoch**: 26/27
- **Best Validation Loss**: 417.3099
- **Best Validation RMSE**: 20.4282 W/m²
- **Peak GPU Memory (VRAM)**: 4434.02 MB

## Test Results

- **MSE Loss**: 392.7802
- **RMSE**: 19.8187 W/m²
- **MAE**: 11.1011 W/m²
- **R² Score**: 0.9947

## Generated Files

- Model checkpoint: `mask_crop_rubsheet_square_model_2026-03-05_20-33.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
