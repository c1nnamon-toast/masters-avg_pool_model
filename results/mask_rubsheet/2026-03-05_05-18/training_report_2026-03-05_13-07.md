# Training Report

**Date**: 2026-03-05 13:07:18

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 8 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_mask_rubsheet |
| Device | cuda |

## Training Results

- **Training Time**: 467.2 minutes
- **Best Epoch**: 25/27
- **Best Validation Loss**: 568.1406
- **Best Validation RMSE**: 23.8357 W/m²
- **Peak GPU Memory (VRAM)**: 16229.50 MB

## Test Results

- **MSE Loss**: 542.2747
- **RMSE**: 23.2868 W/m²
- **MAE**: 13.5328 W/m²
- **R² Score**: 0.9927

## Generated Files

- Model checkpoint: `mask_rubsheet_model_2026-03-05_05-18.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
