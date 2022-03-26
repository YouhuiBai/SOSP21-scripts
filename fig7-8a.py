import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math

# matplotlib.rc('font', family='Times New Roman')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

#mxnet local_56G_ vgg19
labels = ['2', '4', '8', '16', '32']


byteps          =   [190,	298,	474,	821	,1457]
horovod         =   [198,	358,	629,	1194,	2118]
byteps_comp     =   [190,	358,	686,	1345,	2216]
hi_ring_comp    =   [197,	443,	876,	1722,	3374]
hi_ps_comp      =   [198,	449,	881,	1750,	3396]
linear          =   [235,	469,	938,	1877,	3754]

bar_num = 5
x = np.arange(len(labels))  # the label locations
width = 0.1 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 2 * width, byteps, width, label='BytePS', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x - 1 * width, horovod, width, label='Ring', linewidth=0, ec='w',)
rects3 = ax.bar(x + 0 * width, byteps_comp, width, label='BytePS(OSS-onebit)', ec='w',linewidth=0, hatch='-')
rects4 = ax.bar(x + 1 * width, hi_ring_comp, width, label='HiPress-CaSync-Ring(CompLL-onebit)', ec='w', linewidth=0, hatch='/')
rects5 = ax.bar(x + 2 * width, hi_ps_comp, width, label='HiPress-CaSync-PS(CompLL-onebit)', ec='w', linewidth=0, hatch='\\')
linear = ax.bar(x, linear, width * bar_num, color='None', edgecolor='black', label='Linear-Scaling')


# Add some text for labels, title and custom x-axis tick labels, etc.
ratio = 0.52
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
ax.tick_params(axis="y", labelsize=15)
ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.set_ylabel('Images/sec', fontsize=20)
ax.set_xlabel('The Number of GPUs', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=17)
ax.legend(loc=2, frameon=False, fontsize=13)
ax.yaxis.get_offset_text().set_fontsize(14)

fig.tight_layout()
fig.savefig("MXNet_local_56G__1080Ti_VGG19.pdf", bbox_inches="tight")



#mxnet local_56G_ bert
labels = ['2', '4', '8', '16', '32']


byteps          =   [16262,	24368,	41133,	79633	,153701]
horovod         =   [16365,	29344,	54112,	103441,	197521]
byteps_comp     =   [16371,	29339,	51641,	97474	,180782]
hi_ring_comp    =   [16375,	33215,	65094,	126421,	247234]
hi_ps_comp      =   [16365,	33746,	65998,	127872,	254092]
linear          =   [17952,	35905,	71810,	143619,	287238]

bar_num = 5
x = np.arange(len(labels))  # the label locations
width = 0.1 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 2 * width, byteps, width, label='BytePS', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x - 1 * width, horovod, width, label='Ring', linewidth=0, ec='w',)
rects3 = ax.bar(x + 0 * width, byteps_comp, width, label='BytePS(OSS-onebit)', ec='w',linewidth=0, hatch='-')
rects4 = ax.bar(x + 1 * width, hi_ring_comp, width, label='HiPress-CaSync-Ring(CompLL-onebit)', ec='w', linewidth=0, hatch='/')
rects5 = ax.bar(x + 2 * width, hi_ps_comp, width, label='HiPress-CaSync-PS(CompLL-onebit)', ec='w', linewidth=0, hatch='\\')
linear = ax.bar(x, linear, width * bar_num, color='None', edgecolor='black', label='Linear-Scaling')

# Add some text for labels, title and custom x-axis tick labels, etc.
ratio = 0.52
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
ax.tick_params(axis="y", labelsize=15)
ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.set_ylabel('Sequences/sec', fontsize=20)
ax.set_xlabel('The Number of GPUs', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=17)
ax.legend(loc=2, frameon=False, fontsize=13)
ax.yaxis.get_offset_text().set_fontsize(14)

fig.tight_layout()
fig.savefig("MXNet_local_56G__1080Ti_Bert.pdf", bbox_inches="tight")



################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################



#mxnet_AWS_100G_ vgg19
labels = ['8', '16', '32', '64', '128']


byteps          =   [1525 ,	1563, 	2954, 	5800, 	11165 ]
horovod         =   [1562 ,	2349, 	4369, 	8157, 	14655 ]
byteps_comp     =   [1561 ,	2548, 	4424, 	8058, 	13865 ]
hi_ring_comp    =   [1567 	,3043 ,	6053 ,	11921, 	23097 ]
hi_ps_comp      =   [1562 	,3143 ,	6163 ,	12170, 	23507 ]
linear          =   [1652 	,3305 ,	6610 ,	13219, 	26438 ]

bar_num = 5
x = np.arange(len(labels))  # the label locations
width = 0.1 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 2 * width, byteps, width, label='BytePS', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x - 1 * width, horovod, width, label='Ring', linewidth=0, ec='w',)
rects3 = ax.bar(x + 0 * width, byteps_comp, width, label='BytePS(OSS-onebit)', ec='w',linewidth=0, hatch='-')
rects4 = ax.bar(x + 1 * width, hi_ring_comp, width, label='HiPress-CaSync-Ring(CompLL-onebit)', ec='w', linewidth=0, hatch='/')
rects5 = ax.bar(x + 2 * width, hi_ps_comp, width, label='HiPress-CaSync-PS(CompLL-onebit)', ec='w', linewidth=0, hatch='\\')
linear = ax.bar(x, linear, width * bar_num, color='None', edgecolor='black', label='Linear-Scaling')


# Add some text for labels, title and custom x-axis tick labels, etc.
ratio = 0.52
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
ax.tick_params(axis="y", labelsize=15)
ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.set_ylabel('Images/sec', fontsize=20)
ax.set_xlabel('The Number of GPUs', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=17)
ax.legend(loc=2, frameon=False, fontsize=13)
ax.yaxis.get_offset_text().set_fontsize(14)

fig.tight_layout()
fig.savefig("MXNet_AWS_100G__V100_VGG19.pdf", bbox_inches="tight")



#mxnet_AWS_100G_ bert
labels = ['8', '16', '32', '64', '128']


byteps          =   [38452 ,	63615 ,	123287 ,	239858, 	474815 ]
horovod         =   [38452 ,	67834 ,	127391 ,	234441, 	435945 ]
byteps_comp     =   [38453 ,	67913 ,	129593 ,	256815, 	509359 ]
hi_ring_comp    =   [38462 ,	79023 ,	156542 ,	310462, 	606363 ]
hi_ps_comp      =   [38452 ,	80617 ,	162961 ,	319001, 	628083 ]
linear          =   [41620 ,	83241 ,	166481 ,	332963, 	665925 ]

bar_num = 5
x = np.arange(len(labels))  # the label locations
width = 0.1 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 2 * width, byteps, width, label='BytePS', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x - 1 * width, horovod, width, label='Ring', linewidth=0, ec='w',)
rects3 = ax.bar(x + 0 * width, byteps_comp, width, label='BytePS(OSS-onebit)', ec='w',linewidth=0, hatch='-')
rects4 = ax.bar(x + 1 * width, hi_ring_comp, width, label='HiPress-CaSync-Ring(CompLL-onebit)', ec='w', linewidth=0, hatch='/')
rects5 = ax.bar(x + 2 * width, hi_ps_comp, width, label='HiPress-CaSync-PS(CompLL-onebit)', ec='w', linewidth=0, hatch='\\')
linear = ax.bar(x, linear, width * bar_num, color='None', edgecolor='black', label='Linear-Scaling')


# Add some text for labels, title and custom x-axis tick labels, etc.
ratio = 0.52
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
ax.tick_params(axis="y", labelsize=15)
ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.set_ylabel('Sequences/sec', fontsize=20)
ax.set_xlabel('The Number of GPUs', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=17)
ax.legend(loc=2, frameon=False, fontsize=13)
ax.yaxis.get_offset_text().set_fontsize(14)

fig.tight_layout()
fig.savefig("MXNet_AWS_100G__V100_Bert.pdf", bbox_inches="tight")