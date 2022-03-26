import math
import numpy as np
import matplotlib.pyplot as plt

import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

#MXNet 25G vs 100G
labels = ['AWS', 'Local']

low =  [1.434685998, 1.625135386, ]
high = [1.470764154, 1.700791282, ]

offset = 1
bar_num = 2
x = np.arange(len(labels))  # the label locations
width = 0.2 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 1/2 * width, low, width, label='Low Bandwidth', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x + 1/2 * width, high, width, label='High Bandwidth ', linewidth=0, ec='w',)


ratio = 0.68
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)

ax.set_ylabel('Speedups normalized to\nthe BytePS(non-compression)', fontsize=15)
ax.set_xticks(x)
ax.tick_params(axis="y", labelsize=18)
ax.set_xticklabels(labels, fontsize=20)
ax.legend(loc=2,frameon=False, fontsize=15)
ax.yaxis.get_offset_text().set_fontsize(15)
ax.set_ylim([0, 2])
ax.set_xlim([-0.5, 1.5])
fig.tight_layout()
plt.savefig("low_vs_high.pdf", bbox_inches="tight")
