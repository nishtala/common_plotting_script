#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import common

line_1 = [100, 200, 300]
line_2 = [3, 4, 5]

nrows = 1
ncols = 1
fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=common.set_size(fraction=0.33, subplot=[nrows, ncols]))
rects1 = ax.plot(line_1, label='line_1', marker='*')
rects2 =ax.plot(line_2, label='line_2', marker='o', linestyle='--')
for i, j in enumerate(line_2):
    ax.annotate(str(round(j,2)),xy=(i-0.1,j+0.5))

ax.set_yscale('log', basey=2)
ax.legend(loc='upper center', ncol=1, bbox_to_anchor=(0.25, 1.))
plt.xticks(np.arange(3), ('1','2','3'))

ax.set_ylabel('Example $y$-axis')
ax.set_xlabel('Example $x$-axis')

fig.tight_layout()
file_name = 'test.pdf'
fig.savefig(file_name)
fig.clf()
plt.close()

