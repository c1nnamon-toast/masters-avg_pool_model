# Training Report

**Date**: 2026-03-02 22:49:43

## Configuration

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.0001 |
| Batch Size | 16 |
| Epochs | 20 |
| Dataset | /home/xtsimbota_135764/masters/dataset/original |
| Device | cuda |

## Training Results

- **Training Time**: 218.9 minutes
- **Best Validation Loss**: 211.7773
- **Best Validation RMSE**: 14.5526 W/m²
- **Peak GPU Memory (VRAM)**: 20620.22 MB

## Test Results

- **MSE Loss**: 191.2369
- **RMSE**: 13.8288 W/m²
- **MAE**: 9.0248 W/m²
- **R² Score**: 0.9974

## Generated Files

- Model checkpoint: `best_skycnn_model.pth`
- Training curves: `analysis/training_curves.png`
- Predictions plot: `analysis/predictions_vs_actual.png`
- Error distribution: `analysis/error_distribution.png`
