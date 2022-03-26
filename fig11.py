
import matplotlib
# matplotlib.use('Agg')
matplotlib.rc('font', family='Times New Roman')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import pandas
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter



VGG = pandas.DataFrame(dict(graph=['Linear', '+SeCoPa', '+Bulk Sync', '+Pipeline', '+On-GPU', '+On-CPU', 'Default'],
                           base=[0, 114, 114, 113, 116, 114, 113], comp=[0, 276, 276, 277, 282, 275, 274]))
VGG1 = pandas.DataFrame(dict(graph=['Linear', '+SeCoPa', '+Bulk Sync', '+Pipeline', '+On-GPU', '+On-CPU', 'Default'],
                           Sync=[0, 189, 236, 319, 346, 774, 590]))
VGG2 = [x + y for x, y in zip(VGG.base, VGG1.Sync)]



Bert = pandas.DataFrame(dict(graph=['Linear', '+SeCoPa', '+Bulk Sync', '+Pipeline', '+On-GPU', '+On-CPU', 'Default'],
                           base=[0, 234, 235, 235, 237, 0, 234], comp=[0, 459, 460, 459, 470, 0, 458]))
Bert1 = pandas.DataFrame(dict(graph=['Linear', '+SeCoPa', '+Bulk Sync', '+Pipeline', '+On-GPU', '+On-CPU', 'Defaul t'],
                           Sync=[0, 299, 323, 346, 387, 0, 430]))
Bert2 = [x + y for x, y in zip(Bert.base, Bert1.Sync)]

ind = np.arange(len(VGG))
width = 0.4

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,4))

ax1.barh(ind, VGG2, width, color='#ff7f0e', label='Synchronization')
ax1.barh(ind, VGG.base, width, color='w', ec='w')
ax1.barh(ind + width, VGG.comp, width, color='#1f77b4', hatch='x', ec='w', linewidth=0, label='Computation')

ax1.set(yticks=ind + width/2, yticklabels=VGG.graph, ylim=[2*width-1.2, len(VGG)])
linearVal = 273  # Linear value of VGG19
ax1.barh(width/2, linearVal, width, color='#1f77b4', hatch='x', ec='w', linewidth=0)
ax1.legend(fontsize=20,labelspacing=0.1,handletextpad=0.2,columnspacing=1.2)
#ax1.set_xlim([0,15])

ax2.barh(ind, Bert2, width, color='#ff7f0e', label='Synchronization')
ax2.barh(ind, Bert.base, width, color='w', ec='w')
ax2.barh(ind + width, Bert.comp, width, color='#1f77b4', hatch='x', ec='w', linewidth=0, label='Computation')

ax2.set(yticks=ind + width/2, yticklabels=Bert.graph, ylim=[2*width-1.2, len(Bert)])
linearVal = 456  # Linear value of BertBase
ax2.barh(width/2, linearVal, width, color='#1f77b4', hatch='x', ec='w', linewidth=0)
# ax2.legend(fontsize=22,labelspacing=0.1,handletextpad=0.2,columnspacing=1.2)


ax2.set_yticks([])


ax1.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))

ax2.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))


Fontsize = 24
ax1.set_xlabel('Time Cost(ms)', fontsize=Fontsize)
ax1.set_title('VGG19, BytePS vs. CaSync-PS', fontsize=Fontsize)

ax2.set_xlabel('Time Cost(ms)', fontsize=Fontsize)
ax2.set_title('Bert-base, Ring vs. CaSync-Ring', fontsize=Fontsize)

# ax1.set_xlim([0, 1499])
# ax2.set_xlim([0, 1499])

ax1.tick_params(axis="x", labelsize=24)
ax2.tick_params(axis="x", labelsize=24)
ax1.tick_params(axis="y", labelsize=24)
ax2.tick_params(axis="y", labelsize=24)

plt.subplots_adjust(wspace=0.05)

# plt.show()
plt.savefig('opt_breakdown2.pdf', bbox_inches='tight')

