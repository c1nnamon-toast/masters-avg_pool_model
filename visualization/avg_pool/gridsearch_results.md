# Visualization Grid Search Results

**Generated**: 2026-04-23 04:11:17  
**Total runtime**: 13087.9 s (218.1 min)

---

## Results

| # | Experiment | Method | Hyperparameters | Status | Time (s) | Output |
|--:|-----------|--------|-----------------|:------:|----------|--------|
| 1 | Fisheye | IG | n_steps=15 | OK | 63.9 | `visualization/avg_pool/fisheye/ig_nsteps15` |
| 2 | Fisheye | IG | n_steps=20 | OK | 68.6 | `visualization/avg_pool/fisheye/ig_nsteps20` |
| 3 | Fisheye | IG | n_steps=40 | OK | 91.2 | `visualization/avg_pool/fisheye/ig_nsteps40` |
| 4 | Fisheye | IG | n_steps=80 | OK | 137.2 | `visualization/avg_pool/fisheye/ig_nsteps80` |
| 5 | Fisheye | Occlusion | patch=15, stride=12 | OK | 2327.1 | `visualization/avg_pool/fisheye/occ_p15_s12` |
| 6 | Fisheye | Occlusion | patch=15, stride=15 | OK | 1529.7 | `visualization/avg_pool/fisheye/occ_p15_s15` |
| 7 | Fisheye | Occlusion | patch=25, stride=12 | OK | 2275.2 | `visualization/avg_pool/fisheye/occ_p25_s12` |
| 8 | Fisheye | Occlusion | patch=25, stride=15 | OK | 1488.3 | `visualization/avg_pool/fisheye/occ_p25_s15` |
| 9 | Rubsheet 3-to-1 | IG | n_steps=15 | OK | 46.0 | `visualization/avg_pool/rubsheet_3to1/ig_nsteps15` |
| 10 | Rubsheet 3-to-1 | IG | n_steps=20 | OK | 50.6 | `visualization/avg_pool/rubsheet_3to1/ig_nsteps20` |
| 11 | Rubsheet 3-to-1 | IG | n_steps=40 | OK | 68.1 | `visualization/avg_pool/rubsheet_3to1/ig_nsteps40` |
| 12 | Rubsheet 3-to-1 | IG | n_steps=80 | OK | 101.6 | `visualization/avg_pool/rubsheet_3to1/ig_nsteps80` |
| 13 | Rubsheet 3-to-1 | Occlusion | patch=15, stride=12 | OK | 1273.9 | `visualization/avg_pool/rubsheet_3to1/occ_p15_s12` |
| 14 | Rubsheet 3-to-1 | Occlusion | patch=15, stride=15 | OK | 819.2 | `visualization/avg_pool/rubsheet_3to1/occ_p15_s15` |
| 15 | Rubsheet 3-to-1 | Occlusion | patch=25, stride=12 | OK | 1236.6 | `visualization/avg_pool/rubsheet_3to1/occ_p25_s12` |
| 16 | Rubsheet 3-to-1 | Occlusion | patch=25, stride=15 | OK | 797.1 | `visualization/avg_pool/rubsheet_3to1/occ_p25_s15` |
| 17 | Rubsheet Square | IG | n_steps=15 | OK | 32.1 | `visualization/avg_pool/rubsheet_square/ig_nsteps15` |
| 18 | Rubsheet Square | IG | n_steps=20 | OK | 33.0 | `visualization/avg_pool/rubsheet_square/ig_nsteps20` |
| 19 | Rubsheet Square | IG | n_steps=40 | OK | 38.2 | `visualization/avg_pool/rubsheet_square/ig_nsteps40` |
| 20 | Rubsheet Square | IG | n_steps=80 | OK | 48.5 | `visualization/avg_pool/rubsheet_square/ig_nsteps80` |
| 21 | Rubsheet Square | Occlusion | patch=15, stride=12 | OK | 124.6 | `visualization/avg_pool/rubsheet_square/occ_p15_s12` |
| 22 | Rubsheet Square | Occlusion | patch=15, stride=15 | OK | 83.9 | `visualization/avg_pool/rubsheet_square/occ_p15_s15` |
| 23 | Rubsheet Square | Occlusion | patch=25, stride=12 | OK | 119.4 | `visualization/avg_pool/rubsheet_square/occ_p25_s12` |
| 24 | Rubsheet Square | Occlusion | patch=25, stride=15 | OK | 80.0 | `visualization/avg_pool/rubsheet_square/occ_p25_s15` |

**Completed**: 24/24 succeeded, 0 failed

---

## Grid Search Configuration

### Integrated Gradients

| Experiment | n_steps values |
|-----------|----------------|
| Fisheye | 15, 20, 40, 80 |
| Rubsheet 3-to-1 | 15, 20, 40, 80 |
| Rubsheet Square | 15, 20, 40, 80 |

### Occlusion (full cross-product: patch_size x stride)

| Experiment | patch_sizes | strides | combos (stride <= patch) |
|-----------|-------------|---------|--------------------------|
| Fisheye | 15, 25 | 12, 15 | 4 |
| Rubsheet 3-to-1 | 15, 25 | 12, 15 | 4 |
| Rubsheet Square | 15, 25 | 12, 15 | 4 |
