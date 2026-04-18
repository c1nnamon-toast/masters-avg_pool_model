# Training Report

**Date**: 2026-03-04 08:40:58

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 8 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_rubsheet |
| Device | cuda |

## Training Results

- **Training Time**: 467.0 minutes
- **Best Epoch**: 21/27
- **Best Validation Loss**: 199.0577
- **Best Validation RMSE**: 14.1088 W/m²
- **Peak GPU Memory (VRAM)**: 16229.50 MB

## Test Results

- **MSE Loss**: 164.6888
- **RMSE**: 12.8331 W/m²
- **MAE**: 7.6646 W/m²
- **R² Score**: 0.9978

## Generated Files

- Model checkpoint: `rubsheet_model_2026-03-04_00-52.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
