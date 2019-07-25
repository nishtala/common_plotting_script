##### Make stylish LaTeX style plots with matplotlib.

```python
import common
import matplotlib.pyplot as plt
nrows = 1
ncols = 1
fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=common.set_size(fraction=0.33, subplot=[nrows, ncols]))
```

