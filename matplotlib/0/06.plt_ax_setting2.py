# 6 - axis setting

"""
Tutorial reference:
http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)
# plt the second cure in this figure with certain parameters
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

plt.xlabel('I am x')
plt.ylabel('I am y')

# set new ticks
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)

# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
            [r'$really\ bad$', r'$bad\ \alpha$', r'$normal\ alpha$', r'$good$', r'$reall\ good$'])
# to use '$ $' for math text and nice looking, e.g. '$\pi$'

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
# ACCEPTS: ['top' | 'bottom' | 'both' | 'default' | 'none']
ax.spines['bottom'].set_position(('data', 0))
# the 1st is in 'outward' | 'axes' | 'data'
# axes: percentage of y axis
# data: depend on y data

ax.yaxis.set_ticks_position('left')
# ACCEPTS: ['left' | 'right' | 'both' | 'default' | 'none']

ax.spines['left'].set_position(('data', 0))

plt.show()
