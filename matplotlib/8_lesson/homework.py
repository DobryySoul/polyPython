import numpy as np
import pandas as pd
# import matplotlib as mpl
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.pyplot as plt


# График №1
# x = [1, 5, 10, 15, 20]
# y1 = [0.75, 7, 3, 5, 11]
# y2 = [4, 3, 0.75, 8, 12]

# plt.plot(x, y1, color='red', marker='o', label='line 1', linestyle='-')
# plt.plot(x, y2, color='green', marker='o', label='line 1', linestyle='-.')

# plt.legend()


# График №2
# x = [1, 2, 3, 4, 5]
# y1 = [0.1, 7, 6, 3, 5]
# y2 = [9, 4, 2, 4, 9]
# y3 = [-7, -4, 2, -4, -7]

# fig = plt.figure()

# ax1 = fig.add_subplot(2, 1, 1)
# ax1.plot(x, y1)

# ax2 = fig.add_subplot(2, 2, 3)
# ax2.plot(x, y2)

# ax3 = fig.add_subplot(2, 2, 4)
# ax3.plot(x, y3)

# plt.tight_layout()

# График №3
# fig, ax = plt.subplots()
# x = np.linspace(-5, 5, 11)
# ax.plot(x, x**2)

# ax.annotate('min', xy=(0, 0), xytext=(0, 10), arrowprops=dict(facecolor='green'))

# График №4
# data = np.random.randint(11, size=(7, 7))

# fig, ax = plt.subplots()
# im = ax.imshow(data, cmap='viridis', interpolation='nearest')
# # gr = ax.pcolor(data, cmap='viridis')
# ax.invert_yaxis()
# axins = inset_axes(ax,
#                    width="7%",
#                    height="50%",
#                    loc='lower left',
#                    bbox_to_anchor=(1.05, 0., 1, 1),
#                    bbox_transform=ax.transAxes,
#                    borderpad=0,
#                    )

# plt.colorbar(im, cax=axins)

# График №5

# x = np.linspace(0, 5, 1000)
# y = np.sin(np.pi * x + np.pi / 2)

# plt.fill_between(x, y, color='blue') # Разобраться с цветом
# plt.plot(x, y, color='red')

# plt.ylim(-1.1, 1.1)

# График №6 # ДОДЕЛАТЬ
x = np.linspace(0, 4 * np.pi, 100)
y = np.cos(x)

# y[y < -0.5] = -0.5
# y[y > 1.0] = 1.0

plt.plot(x, y)
plt.ylim(-1, 1)  
# plt.xticks([0, 4])  

plt.show()