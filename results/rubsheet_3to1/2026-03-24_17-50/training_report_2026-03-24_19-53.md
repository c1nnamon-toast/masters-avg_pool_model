# Training Report

**Date**: 2026-03-24 19:53:46

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 15 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_rubsheet_3to1 |
| Device | cuda |

## Training Results

- **Training Time**: 123.1 minutes
- **Best Epoch**: 13/15
- **Best Validation Loss**: 646.7794
- **Best Validation RMSE**: 25.4319 W/m²
- **Peak GPU Memory (VRAM)**: 15308.87 MB

## Test Results

- **MSE Loss**: 615.8716
- **RMSE**: 24.8168 W/m²
- **MAE**: 15.0359 W/m²
- **R² Score**: 0.9917

## Generated Files

- Model checkpoint: `rubsheet_3to1_model_gap_2026-03-24_17-50.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
