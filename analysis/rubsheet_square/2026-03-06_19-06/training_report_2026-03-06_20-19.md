# Training Report

**Date**: 2026-03-06 20:19:27

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 27 |
| Dataset | /home/xtsimbota_135764/masters/dataset/dataset_rubsheet_square |
| Device | cuda |

## Training Results

- **Training Time**: 72.7 minutes
- **Best Epoch**: 27/27
- **Best Validation Loss**: 140.4078
- **Best Validation RMSE**: 11.8494 W/m²
- **Peak GPU Memory (VRAM)**: 5320.09 MB

## Test Results

- **MSE Loss**: 111.5914
- **RMSE**: 10.5637 W/m²
- **MAE**: 6.1948 W/m²
- **R² Score**: 0.9985

## Generated Files

- Model checkpoint: `rubsheet_square_model_2026-03-06_19-06.pth`
- Training curves: `training_curves.png`
- Predictions plot: `predictions_vs_actual.png`
- Error distribution: `error_distribution.png`
