import numpy as np
import pandas as pd
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

# grid = plt.GridSpec(2, 2)

# plt.subplot(grid[0, 0:])
# plt.plot(x, y1)

# plt.subplot(grid[1, 0])
# plt.plot(x, y2)

# plt.subplot(grid[1, 1])
# plt.plot(x, y3)


# График №3
# fig, ax = plt.subplots()
# x = np.linspace(-5, 5, 11)
# ax.plot(x, x**2)

# ax.annotate('min', xy=(0, 0), xytext=(0, 10), arrowprops=dict(facecolor='green'))


# График №4
# data = np.random.randint(11, size=(7, 7))

# fig, ax = plt.subplots()

# fig.subplots_adjust(right=0.8)
# gr = ax.pcolor(data, cmap='viridis')

# axins = inset_axes(ax,
#                    width="7%",
#                    height="50%",
#                    loc='lower left',
#                    bbox_to_anchor=(1.05, 0., 1, 1),
#                    bbox_transform=ax.transAxes,
#                    borderpad=0,
#                    )

# plt.colorbar(gr, cax=axins)


# График №5
# x = np.linspace(0, 5, 1000)
# y = np.sin(np.pi * x + np.pi / 2)

# plt.fill_between(x, y)
# plt.plot(x, y, color='red')

# plt.ylim(-1.1, 1.1)


# График №6
# x = np.linspace(0, 5, 10000)
# y = np.cos(x * np.pi)

# y[y < -0.5] = np.nan
# y[y > 1.0] = np.nan

# plt.plot(x, y, linewidth=3)
# plt.xticks(np.linspace(0, 4, 5))
# plt.ylim(-1.0, 1.0)  
# plt.xlim(-0.2, 5.0)


# График №7
# x = np.linspace(0, 6, 7)
# y = np.array([0, 1, 2, 3, 4, 5, 6])

# fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# axs[0].step(x, y, where='pre', marker='o', color='green')
# axs[1].step(x, y, where='post', marker='o', color='green')
# axs[2].step(x, y, where='mid', marker='o', color='green')

# for ax in axs:
#     ax.grid(True)
#     ax.set_xlim(-0.25, 6.25)
#     ax.set_ylim(-0.25, 6.25)

# plt.tight_layout()


# График №8
# x = np.linspace(0, 10, 9)
# y1 = -0.2*(x-5)**2 + 5.0
# y2 = -0.6*(x-5)**2 + 15.0
# y3 = -0.55*(x-7)**2 + 27.0

# plt.fill_between(x, y1, label='y1', zorder=3)
# plt.fill_between(x, y2, color="orange", label='y2', zorder=2)
# plt.fill_between(x, y3, color="forestgreen", label='y3', zorder=1)

# plt.legend()

# plt.xlim(-0.3, 10)
# plt.ylim(0, 28)


# График №9
# labels = ['BMW', 'AUDI', 'Jaguar', 'Ford', 'Toyota']
# sizes = [35, 12.5, 22.5, 17.5, 10]
# colors = ['green', 'red', 'purple', 'blue', 'orange']
# explode = [0.1, 0, 0, 0, 0]

# plt.figure(figsize=(5, 5))
# plt.pie(sizes, labels=labels, colors=colors, startangle=100, explode=explode, textprops={'fontsize': 11})

# plt.axis('equal') 


# График №10
# labels = ['BMW', 'AUDI', 'Jaguar', 'Ford', 'Toyota']
# sizes = [35, 12.5, 22.5, 17.5, 10]
# colors = ['green', 'red', 'purple', 'blue', 'orange']
# explode = [0.1, 0, 0, 0, 0]

# plt.figure(figsize=(5, 5))
# plt.pie(sizes, labels=labels, colors=colors, startangle=100, textprops={'fontsize': 11})

# circle = plt.Circle((0, 0), 0.50, fc='white')
# fig = plt.gcf()
# fig.gca().add_artist(circle)

# plt.axis('equal') 

plt.show()