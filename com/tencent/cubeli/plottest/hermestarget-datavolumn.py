# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体

n_groups = 2
data_number = (7600,500)
fig, ax = plt.subplots()
# index = np.arange(n_groups)
bar_width = 0.25

ind = np.linspace(0.5, 1, 2)

opacity = 0.4
rects1 = plt.bar(ind - bar_width / 2, data_number, bar_width,color='green')
plt.ylabel(u'日接入量',fontsize=20)
plt.title(u'日接入量(单位：亿)',fontsize=20)

plt.xticks(ind - bar_width / 2, (u'Herme1.0 实时',u'Hermes2.0 离线'),fontsize=20)
plt.ylim(0, 10000)
plt.legend()

# plt.grid()
# plt.annotate('nlog(n)', xy=(0.1, 7900), xytext=(11, 7),
#                  arrowprops=dict(facecolor='black', shrink=0.06),
#                  )

plt.tight_layout()
plt.show()
