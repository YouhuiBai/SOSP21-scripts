import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# matplotlib.rc('font', family='Times New Roman')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
#MXNet 25G vs 100G
labels = ['Bert-base', 'VGG19']

Ring                                = [1.28509826,  1.453552288]
BytePS_OSS_onebit                   = [1.176189166,	1.520721464]
HiPress_CaSync_Ring_CompLL_onebit   = [1.608536242,	2.315674259]
HiPress_CaSync_PS_CompLL_onebit     = [1.653155512,	2.330647873]
Linear_Scaling                      = [1.868808905,	2.575845954]


bar_num = 4
x = np.arange(len(labels))  # the label locations
width = 0.125 # the width of the bars

fig, ax = plt.subplots()
fig.set_size_inches(10,5)


rects1 = ax.bar(x - 2 * width + 0.5 * width, Ring, width, label='Ring', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x - 1 * width + 0.5 * width, BytePS_OSS_onebit, width, label='BytePS(OSS-onebit)', linewidth=0, ec='w',)
rects4 = ax.bar(x + 1 * width - 0.5 * width, HiPress_CaSync_Ring_CompLL_onebit, width, label='HiPress-CaSync-Ring(CompLL-onebit)', ec='w', linewidth=0, hatch='-')
rects5 = ax.bar(x + 2 * width - 0.5 * width, HiPress_CaSync_PS_CompLL_onebit, width, label='HiPress-CaSync-PS(CompLL-onebit)', ec='w',linewidth=0, hatch='/' )
linear = ax.bar(x, Linear_Scaling, width * bar_num, color='None', edgecolor='black', label='Linear-Scaling')



ratio = 0.7
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)

ax.set_ylabel('Speedups normalized to\nthe BytePS(non-compression)', fontsize=21)
ax.set_xticks(x)
ax.tick_params(axis="y", labelsize=20)
ax.set_xticklabels(labels, fontsize=24)
ax.legend(loc=2, frameon=False, fontsize=13.5)
#ax.legend(bbox_to_anchor=(1.05,1.0), frameon=False, fontsize=10)
ax.yaxis.get_offset_text().set_fontsize(15)
ax.set_ylim([0, 3])
ax.set_xlim([-0.7, 1.65])
fig.tight_layout()
plt.savefig("eval_mxnet_local.pdf", bbox_inches="tight")
