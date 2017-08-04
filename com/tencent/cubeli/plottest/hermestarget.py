# coding: utf-8
# -*- coding: utf-8 -*-
#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

xcord = ["Hermes 1.0", "Hermes 2.0"]
y1cord = [710,461]

# width = 0.4
# fig = plt.figure(1)
# ax = fig.add_subplot(111)
# ind = np.linspace(0.5, 2, 2)
# ax.bar(ind - width / 2, y1cord, width, color='green')
# ax.set_xticks(ind)
# ax.set_xticklabels(xcord)
# plt.show()

#===============================================================
n_groups = 2

server_number = (710,461)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
rects1 = plt.bar(index, server_number, bar_width, alpha=opacity, color='green')
plt.xlabel('Hermes Version')
plt.ylabel('server number')
plt.title('server number')

plt.xticks(index, ('Herme1.0','Hermes2.0'))
plt.ylim(0, 1000)
plt.legend()

plt.tight_layout()
plt.show()
#===============================================================



# # -*- coding: utf-8 -*-
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib as mpl
#
#
# def draw_bar(labels, quants):
#     width = 0.4
#     ind = np.linspace(0.5, 9.5, 10)
#     # make a square figure
#     fig = plt.figure(1)
#     ax = fig.add_subplot(111)
#     # Bar Plot
#     ax.bar(ind - width / 2, quants, width, color='green')
#     # Set the ticks on x-axis
#     ax.set_xticks(ind)
#     ax.set_xticklabels(labels)
#     # labels
#     ax.set_xlabel('Country')
#     ax.set_ylabel('GDP (Billion US dollar)')
#     # title
#     ax.set_title('Top 10 GDP Countries', bbox={'facecolor': '0.8', 'pad': 5})
#     plt.grid(True)
#     plt.show()
#     plt.savefig("bar.jpg")
#     plt.close()
#
#
# labels = ['USA', 'China', 'India', 'Japan', 'Germany', 'Russia', 'Brazil', 'UK', 'France', 'Italy']
#
# quants = [15094025.0, 11299967.0, 4457784.0, 4440376.0, 3099080.0, 2383402.0, 2293954.0, 2260803.0, 2217900.0,
#           1846950.0]
#
# draw_bar(labels, quants)