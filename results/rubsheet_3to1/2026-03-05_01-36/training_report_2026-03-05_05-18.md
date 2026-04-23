# Training Report

**Date**: 2026-03-05 05:18:51

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_rubsheet_3to1 |
| Device | cuda |

## Training Results

- **Training Time**: 222.0 minutes
- **Best Epoch**: 24/27
- **Best Validation Loss**: 179.8682
- **Best Validation RMSE**: 13.4115 W/m²
- **Peak GPU Memory (VRAM)**: 15510.16 MB

## Test Results

- **MSE Loss**: 146.4957
- **RMSE**: 12.1035 W/m²
- **MAE**: 7.2827 W/m²
- **R² Score**: 0.9980

## Generated Files

- Model checkpoint: `rubsheet_3to1_model_2026-03-05_01-36.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
