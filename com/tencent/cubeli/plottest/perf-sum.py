# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体

x1=[8,16,32,64,128]
y1=[9859,5773,4985,3276,3140]
y2=[759,1186,1327,1466,2045]
plt.plot(x1,y1,label=u'单索引耗时',linewidth=3,color='r',marker='o',markerfacecolor='blue',markersize=12)
plt.plot(x1,y2,label=u'整体耗时',linewidth=3,color='b',marker='+',markerfacecolor='red',markersize=12)
plt.xlabel('Thread Number',fontsize=20)
plt.ylabel('Time(ms)')
plt.title(u'单索引耗时和整体耗时\n随线程数变化')
plt.xticks()
plt.legend()
plt.grid()
plt.show()