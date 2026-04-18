# Training Report

**Date**: 2026-03-05 20:33:17

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 8 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_mask_crop_rubsheet |
| Device | cuda |

## Training Results

- **Training Time**: 372.0 minutes
- **Best Epoch**: 25/27
- **Best Validation Loss**: 512.0545
- **Best Validation RMSE**: 22.6286 W/m²
- **Peak GPU Memory (VRAM)**: 13404.00 MB

## Test Results

- **MSE Loss**: 471.8001
- **RMSE**: 21.7210 W/m²
- **MAE**: 11.8662 W/m²
- **R² Score**: 0.9936

## Generated Files

- Model checkpoint: `mask_crop_rubsheet_model_2026-03-05_14-20.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
