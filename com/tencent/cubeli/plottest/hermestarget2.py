import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import matplotlib.pyplot as plt
import numpy as np

n_groups = 2
server_number = (500,7600)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
rects1 = plt.bar(index, server_number, bar_width, alpha=opacity, color='green')
plt.xlabel('Hermes Version')
plt.ylabel('data volumn')
plt.title('data volumn')

plt.xticks(index, ('Herme1.0','Hermes2.0'))
plt.ylim(0, 10000)
plt.legend()

plt.tight_layout()
plt.show()
