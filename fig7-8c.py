import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# matplotlib.rc('font', family='Times New Roman')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

#Pytorch local_56G__1080Ti_ UGATIT
labels = ['2', '4', '8', '16', '32']

byteps = [2.16,	3.60,	6.99,	12.54,	21.31]
Horovod = [2.17,	4.00,	7.67,	15.08,	28.16]
hipress_terngrad = [2.17,	4.33,	8.52,	16.48,	31.91]
linear =  [2.33,	4.67,	9.33,	18.67,	37.34]


bar_num = 3
x = np.arange(len(labels))  # the label locations
width = 0.12 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 1 * width, byteps, width, label='BytePS', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x, Horovod, width, label='Ring', linewidth=0, ec='w',)
rects3 = ax.bar(x + 1 * width, hipress_terngrad, width, label='HiPress-CaSync-PS(CompLL-TernGrad)', ec='w',linewidth=0, hatch='-')
linear = ax.bar(x, linear, width * bar_num, color='None', edgecolor='black', label='Linear-Scaling')


# Add some text for labels, title and custom x-axis tick labels, etc.
ratio = 0.52
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)

ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')

ax.set_ylabel('Images/sec', fontsize=20)
ax.set_xlabel('The Number of GPUs', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=17)
ax.legend(loc=2, frameon=False, fontsize=13)
ax.tick_params(axis="y", labelsize=15)
ax.yaxis.get_offset_text().set_fontsize(14)
fig.tight_layout()

plt.savefig("Pytorch_local_56G__1080Ti_UGATIT.pdf", bbox_inches="tight")


#Pytorch local_56G__1080Ti_ LSTM
labels = ['2', '4', '8', '16', '32']

byteps = [373,	520,	1010,	1897,	3381]
Horovod = [374,	624,	1167,	2226,	4033]
hipress_terngrad = [374,	755,	1470,	2883,	5597]
linear = [400,	799,	1598,	3196,	6392]


bar_num = 3
x = np.arange(len(labels))  # the label locations
width = 0.12 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 1 * width, byteps, width, label='BytePS', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x, Horovod, width, label='Ring', linewidth=0, ec='w',)
rects3 = ax.bar(x + 1 * width, hipress_terngrad, width, label='HiPress-CaSync-PS(CompLL-TernGrad)', ec='w',linewidth=0, hatch='-')
linear = ax.bar(x, linear, width * bar_num, color='None', edgecolor='black', label='Linear-Scaling')


# Add some text for labels, title and custom x-axis tick labels, etc.
ratio = 0.52
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)

ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.set_ylabel('Sequences/sec', fontsize=20)
ax.set_xlabel('The Number of GPUs', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=17)
ax.legend(loc=2, frameon=False, fontsize=13)
ax.tick_params(axis="y", labelsize=15)
ax.yaxis.get_offset_text().set_fontsize(14)
fig.tight_layout()

plt.savefig("Pytorch_local_56G__1080Ti_LSTM.pdf", bbox_inches="tight")


#Pytorch_AWS_100G__V100_ UGATIT
labels = ['8', '16', '32', '64', '128']

byteps              = [16.62, 	18.19 ,	33.14, 	62.21 ,	120.24 ]
Horovod             = [16.62, 	23.28 ,	41.61, 	78.95 ,	149.34 ]
hipress_terngrad    = [16.62 ,	33.57 	,65.75 ,	128.66 ,	250.92 ]
linear              = [17.25 ,	34.49 	,68.98 ,	137.96 ,	275.92 ]




bar_num = 3
x = np.arange(len(labels))  # the label locations
width = 0.12 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 1 * width, byteps, width, label='BytePS', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x, Horovod, width, label='Ring', linewidth=0, ec='w',)
rects3 = ax.bar(x + 1 * width, hipress_terngrad, width, label='HiPress-CaSync-PS(CompLL-TernGrad)', ec='w',linewidth=0, hatch='-')
linear = ax.bar(x, linear, width * bar_num, color='None', edgecolor='black', label='Linear-Scaling')


# Add some text for labels, title and custom x-axis tick labels, etc.
ratio = 0.52
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)

ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')

ax.set_ylabel('Images/sec', fontsize=20)
ax.set_xlabel('The Number of GPUs', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=17)
ax.legend(loc=2, frameon=False, fontsize=13)
ax.tick_params(axis="y", labelsize=15)
ax.yaxis.get_offset_text().set_fontsize(14)
fig.tight_layout()

plt.savefig("Pytorch_AWS_100G__V100_UGATIT.pdf", bbox_inches="tight")



#Pytorch_AWS_100G__V100_ LSTM
labels = ['8', '16', '32', '64', '128']


byteps              = [2558, 	3472, 	6512 ,	12465, 	23671 ]
Horovod             = [2583, 	4298, 	8328 ,	15326, 	27837 ]
hipress_terngrad    = [2583 ,	5271 ,	10206 ,	19780, 	38382 ]
linear              = [2735 ,	5469 ,	10939 ,	21878, 	43756 ]


bar_num = 3
x = np.arange(len(labels))  # the label locations
width = 0.12 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 1 * width, byteps, width, label='BytePS', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x, Horovod, width, label='Ring', linewidth=0, ec='w',)
rects3 = ax.bar(x + 1 * width, hipress_terngrad, width, label='HiPress-CaSync-PS(CompLL-TernGrad)', ec='w',linewidth=0, hatch='-')
linear = ax.bar(x, linear, width * bar_num, color='None', edgecolor='black', label='Linear-Scaling')


# Add some text for labels, title and custom x-axis tick labels, etc.
ratio = 0.52
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.set_ylabel('Sequences/sec', fontsize=20)
ax.set_xlabel('The Number of GPUs', fontsize=20)
ax.set_xticks(x)
ax.yaxis.get_offset_text().set_fontsize(14)
ax.set_xticklabels(labels, fontsize=17)
ax.legend(loc=2, frameon=False, fontsize=13)
ax.tick_params(axis="y", labelsize=15)
fig.tight_layout()

plt.savefig("Pytorch_AWS_100G__V100_LSTM.pdf", bbox_inches="tight")