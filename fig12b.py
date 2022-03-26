import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

#MXNet 25G vs 100G
labels = ['2bits 4bits 8bits\nTernGrad', '0.001 0.01 0.05\nDGC']

onebar = [3238.54, 3378.69]
twobar = [2824.47, 3151.42]
threebar = [2475.67, 2998.04]


offset = 1
bar_num = 3
x = np.arange(len(labels))  # the label locations
width = 0.2 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x -  width, onebar, width,  linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x , twobar, width,  linewidth=0, ec='w',)
rects2 = ax.bar(x + width, threebar, width, linewidth=0, ec='w', hatch='-')


ratio = 0.68
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.set_ylabel('Images/sec', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=15)
ax.tick_params(axis="y", labelsize=18)
ax.yaxis.get_offset_text().set_fontsize(15)
#ax.legend(frameon=False, fontsize=15)

ax.set_xlim([-0.6, 1.6])
fig.tight_layout()
plt.savefig("compression_rate.pdf", bbox_inches="tight")
