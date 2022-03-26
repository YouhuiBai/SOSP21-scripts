import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# matplotlib.rc('font', family='Times New Roman')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

#TF local_56G__1080Ti_ ResNet50
labels = ['2', '4', '8', '16', '32']

byteps = [363,	711,	1406,	2650,	4732]
horovod = [362,	701,	1366,	2751,	4844]
tf_dgc =[363,	713,	1398,	2770,	5053]
hipress_dgc = [362,	745,	1473,	2902,	5645]
linear = [389,	778,	1555,	3110,	6221]


bar_num = 4
x = np.arange(len(labels))  # the label locations
width = 0.12 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 2 * width + 0.5 * width, byteps, width, label='BytePS', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x - 1 * width + 0.5 * width, horovod, width, label='Ring', linewidth=0, ec='w',)
rects4 = ax.bar(x + 1 * width - 0.5 * width, tf_dgc, width, label='Ring(OSS-DGC)', ec='w', linewidth=0, hatch='-')
rects5 = ax.bar(x + 2 * width - 0.5 * width, hipress_dgc, width, label='HiPress-CaSync-Ring(CompLL-DGC)', ec='w',linewidth=0, hatch='/' )
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

plt.savefig("TF_local_56G__1080Ti_ResNet50.pdf", bbox_inches="tight")




#TF local_56G__1080Ti_ transformer
labels = ['2', '4', '8', '16', '32']



byteps = [18043,	25932,	50138,	97904	,189472]
horovod = [18439,	29702,	57171,	110606,	213084]
tf_dgc = [18345,	32743,	62466,	120743,	230740]
hipress_dgc =[18533,	38548,	75705,	146484,	288852]
linear = [20865,	41730,	83460,	166920,	333839]


bar_num = 4
x = np.arange(len(labels))  # the label locations
width = 0.12 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 2 * width + 0.5 * width, byteps, width, label='BytePS', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x - 1 * width + 0.5 * width, horovod, width, label='Ring', linewidth=0, ec='w',)
rects4 = ax.bar(x + 1 * width - 0.5 * width, tf_dgc, width, label='Ring(OSS-DGC)', ec='w', linewidth=0, hatch='-')
rects5 = ax.bar(x + 2 * width - 0.5 * width, hipress_dgc, width, label='HiPress-CaSync-Ring(CompLL-DGC)', ec='w',linewidth=0, hatch='/' )
linear = ax.bar(x, linear, width * bar_num, color='None', edgecolor='black', label='Linear-Scaling')


# Add some text for labels, title and custom x-axis tick labels, etc.
ratio = 0.52
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.set_ylabel('Tokens/sec', fontsize=20)
ax.set_xlabel('The Number of GPUs', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=17)
ax.legend(loc=2, frameon=False, fontsize=13)
ax.yaxis.get_offset_text().set_fontsize(14)
ax.tick_params(axis="y", labelsize=15)
fig.tight_layout()

plt.savefig("TF_local_56G__1080Ti_transformer.pdf", bbox_inches="tight")



#TF_AWS_100G__V100_ ResNet50
labels = ['8', '16', '32', '64', '128']


byteps      = [2484, 	4619, 	8888 ,	17503 ,	32198 ]
horovod     = [2490, 	4797, 	9254 ,	18099 ,	33133 ]
tf_dgc      = [2490, 	4757, 	9125 ,	17963 ,	33168 ]
hipress_dgc = [2490, 	5061, 	10009, 	19652, 	38864] 
linear      = [2622, 	5243, 	10486, 	20973, 	41946] 



bar_num = 4
x = np.arange(len(labels))  # the label locations
width = 0.12 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 2 * width + 0.5 * width, byteps, width, label='BytePS', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x - 1 * width + 0.5 * width, horovod, width, label='Ring', linewidth=0, ec='w',)
rects4 = ax.bar(x + 1 * width - 0.5 * width, tf_dgc, width, label='Ring(OSS-DGC)', ec='w', linewidth=0, hatch='-')
rects5 = ax.bar(x + 2 * width - 0.5 * width, hipress_dgc, width, label='HiPress-CaSync-Ring(CompLL-DGC)', ec='w',linewidth=0, hatch='/' )
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

plt.savefig("TF_AWS_100G__V100_ResNet50.pdf", bbox_inches="tight")



#TF_AWS_100G__V100_ transformer
labels = ['8', '16', '32', '64', '128']



byteps          = [115332, 	168699,	270642, 	545997 ,	944255 ]
horovod         = [123021, 	199415,	354411, 	633834 ,	1108166 ]
tf_dgc          = [123033, 	221033,	408730, 	773047 ,	1347943 ]
hipress_dgc     = [122442, 	268094,	513715, 	994966 ,	1901843 ]
linear          = [139131, 	278261,	556522, 	1113044, 	2226089 ]

bar_num = 4
x = np.arange(len(labels))  # the label locations
width = 0.12 # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - 2 * width + 0.5 * width, byteps, width, label='BytePS', linewidth=0, ec='w',hatch='x')
rects2 = ax.bar(x - 1 * width + 0.5 * width, horovod, width, label='Ring', linewidth=0, ec='w',)
rects4 = ax.bar(x + 1 * width - 0.5 * width, tf_dgc, width, label='Ring(OSS-DGC)', ec='w', linewidth=0, hatch='-')
rects5 = ax.bar(x + 2 * width - 0.5 * width, hipress_dgc, width, label='HiPress-CaSync-Ring(CompLL-DGC)', ec='w',linewidth=0, hatch='/' )
linear = ax.bar(x, linear, width * bar_num, color='None', edgecolor='black', label='Linear-Scaling')

# Add some text for labels, title and custom x-axis tick labels, etc.
ratio = 0.52
xleft, xright = ax.get_xlim()
ybottom, ytop = ax.get_ylim()
ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
ax.set_ylabel('Tokens/sec', fontsize=20)
ax.set_xlabel('The Number of GPUs', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=17)
ax.legend(loc=2, frameon=False, fontsize=13)
ax.tick_params(axis="y", labelsize=15)
ax.yaxis.get_offset_text().set_fontsize(14)
fig.tight_layout()

plt.savefig("TF_AWS_100G__V100_transformer.pdf", bbox_inches="tight")