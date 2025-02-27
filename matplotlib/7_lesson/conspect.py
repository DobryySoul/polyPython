import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# fig, ax = plt.subplots(2, 3)
# fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')

# for i in range(2):
#     for j in range(3):
#         ax[i, j].text(0.5, 0.5, str((i, j)), fontsize=16, 
#         ha='center')


# grid = plt.GridSpec(2, 3)

# plt.subplot(grid[:2, 0])
# plt.subplot(grid[0, 1:])
# plt.subplot(grid[1, 1])
# plt.subplot(grid[1, 2])


# mean = [0, 0]
# cov = [[1, 1], [1, 2]]

# rng = np.random.default_rng(1)
# x, y = rng.multivariate_normal(mean, cov, 3000).T

# fig = plt.figure()
# grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.5)

# main_ax = fig.add_subplot(grid[:-1, 1:])

# y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)

# x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)

# y_hist.hist(y, 40, orientation='horizontal', color='gray', histtype='stepfilled')

# x_hist.hist(x, 40, orientation='vertical', color='gray', histtype='step')


## Поясняющие надписи

births = pd.read_csv('births-1969.csv')


plt.show()