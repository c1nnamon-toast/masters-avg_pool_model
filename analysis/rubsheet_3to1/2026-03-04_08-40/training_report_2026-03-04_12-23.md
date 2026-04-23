# Training Report

**Date**: 2026-03-04 12:23:47

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_rubsheet_3to1 |
| Device | cuda |

## Training Results

- **Training Time**: 222.2 minutes
- **Best Epoch**: 19/27
- **Best Validation Loss**: 197.9026
- **Best Validation RMSE**: 14.0678 W/m²
- **Peak GPU Memory (VRAM)**: 15510.16 MB

## Test Results

- **MSE Loss**: 173.3408
- **RMSE**: 13.1659 W/m²
- **MAE**: 7.6031 W/m²
- **R² Score**: 0.9977

## Generated Files

- Model checkpoint: `rubsheet_3to1_model_2026-03-04_08-40.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
