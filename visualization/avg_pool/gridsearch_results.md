# Visualization Grid Search Results

**Generated**: 2026-03-24 00:58:31  
**Total runtime**: 342.5 s (5.7 min)

---

## Results

| # | Experiment | Method | Hyperparameters | Status | Time (s) | Output |
|--:|-----------|--------|-----------------|:------:|----------|--------|
| 1 | Fisheye | IG | n_steps=15 | OK | 83.5 | `analysis/viz_gridsearch/fisheye/ig_nsteps15` |
| 2 | Fisheye | IG | n_steps=20 | FAIL | 0.2 | `analysis/viz_gridsearch/fisheye/ig_nsteps20` |
| 3 | Fisheye | IG | n_steps=25 | FAIL | 0.5 | `analysis/viz_gridsearch/fisheye/ig_nsteps25` |
| 4 | Rubsheet 3-to-1 | IG | n_steps=15 | OK | 57.5 | `analysis/viz_gridsearch/rubsheet_3to1/ig_nsteps15` |
| 5 | Rubsheet 3-to-1 | IG | n_steps=20 | OK | 70.7 | `analysis/viz_gridsearch/rubsheet_3to1/ig_nsteps20` |
| 6 | Rubsheet 3-to-1 | IG | n_steps=25 | FAIL | 0.2 | `analysis/viz_gridsearch/rubsheet_3to1/ig_nsteps25` |

**Completed**: 3/6 succeeded, 3 failed

## Failures

### Fisheye / IG / n_steps=20

```
Traceback (most recent call last):
  File "/home/xtsimbota_135764/masters/main_viz.py", line 459, in main
    run_ig_trial(
  File "/home/xtsimbota_135764/masters/main_viz.py", line 228, in run_ig_trial
    attributions = ig.attribute(inp, baseline, n_steps=n_steps, target=0)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/log/dummy_log.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/attr/_core/integrated_gradients.py", line 289, in attribute
    attributions = self._attribute(
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/attr/_core/integrated_gradients.py", line 368, in _attribute
    grads = self.gradient_func(
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/_utils/gradient.py", line 128, in compute_gradients
    outputs = _run_forward(forward_fn, inputs, target_ind, additional_forward_args)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/_utils/common.py", line 588, in _run_forward
    output = forward_func(
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/nn/model.py", line 56, in forward
    x = self.pool4(self.conv_block4(x))
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 346.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 20.69 MiB is free. Including non-PyTorch memory, this process has 23.45 GiB memory in use. Of the allocated memory 22.96 GiB is allocated by PyTorch, and 29.22 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)

```

### Fisheye / IG / n_steps=25

```
Traceback (most recent call last):
  File "/home/xtsimbota_135764/masters/main_viz.py", line 459, in main
    run_ig_trial(
  File "/home/xtsimbota_135764/masters/main_viz.py", line 228, in run_ig_trial
    attributions = ig.attribute(inp, baseline, n_steps=n_steps, target=0)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/log/dummy_log.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/attr/_core/integrated_gradients.py", line 289, in attribute
    attributions = self._attribute(
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/attr/_core/integrated_gradients.py", line 368, in _attribute
    grads = self.gradient_func(
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/_utils/gradient.py", line 128, in compute_gradients
    outputs = _run_forward(forward_fn, inputs, target_ind, additional_forward_args)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/_utils/common.py", line 588, in _run_forward
    output = forward_func(
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/nn/model.py", line 54, in forward
    x = self.pool2(self.conv_block2(x))
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/batchnorm.py", line 193, in forward
    return F.batch_norm(
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/functional.py", line 2812, in batch_norm
    return torch.batch_norm(
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.70 GiB. GPU 0 has a total capacity of 23.52 GiB of which 1.33 GiB is free. Including non-PyTorch memory, this process has 22.14 GiB memory in use. Of the allocated memory 21.66 GiB is allocated by PyTorch, and 15.86 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)

```

### Rubsheet 3-to-1 / IG / n_steps=25

```
Traceback (most recent call last):
  File "/home/xtsimbota_135764/masters/main_viz.py", line 459, in main
    run_ig_trial(
  File "/home/xtsimbota_135764/masters/main_viz.py", line 228, in run_ig_trial
    attributions = ig.attribute(inp, baseline, n_steps=n_steps, target=0)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/log/dummy_log.py", line 39, in wrapper
    return func(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/attr/_core/integrated_gradients.py", line 289, in attribute
    attributions = self._attribute(
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/attr/_core/integrated_gradients.py", line 368, in _attribute
    grads = self.gradient_func(
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/_utils/gradient.py", line 128, in compute_gradients
    outputs = _run_forward(forward_fn, inputs, target_ind, additional_forward_args)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/captum/_utils/common.py", line 588, in _run_forward
    output = forward_func(
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/nn/model.py", line 56, in forward
    x = self.pool4(self.conv_block4(x))
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/modules/pooling.py", line 213, in forward
    return F.max_pool2d(
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/_jit_internal.py", line 624, in fn
    return if_false(*args, **kwargs)
  File "/home/xtsimbota_135764/masters/__venv__dp/lib/python3.10/site-packages/torch/nn/functional.py", line 830, in _max_pool2d
    return torch.max_pool2d(input, kernel_size, stride, padding, dilation, ceil_mode)
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 162.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 58.69 MiB is free. Including non-PyTorch memory, this process has 23.41 GiB memory in use. Of the allocated memory 22.84 GiB is allocated by PyTorch, and 105.99 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)

```

---

## Grid Search Configuration

### Integrated Gradients

| Experiment | n_steps values |
|-----------|----------------|
| Fisheye | 15, 20, 25 |
| Rubsheet 3-to-1 | 15, 20, 25 |

### Occlusion (full cross-product: patch_size x stride)

| Experiment | patch_sizes | strides | combos (stride <= patch) |
|-----------|-------------|---------|--------------------------|
| Fisheye | - | - | - |
| Rubsheet 3-to-1 | - | - | - |
