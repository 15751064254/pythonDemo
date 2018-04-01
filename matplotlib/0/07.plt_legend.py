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

l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')

# plt.legend(loc='upper right')
plt.legend(handles=[l1, l2], labels=['up', 'down'], loc='best')
# the "," is very important in here l1, = plt... and l2, = plt... for this step
"""
legend(handles=(line1, line2, line3),
        labels=('label1', 'label2', 'label3'),
        'upper right')
    The *loc* location codes are::
        'best' : 0,     (currently not supported for figure legends)
        'upper right'   : 1,
        'upper left'    : 2,
        'lower left'    : 3,
        'lower right'   : 4,
        'right'         : 5,
        'center left'   : 6,
        'center right'  : 7,
        'lower center'  : 8,
        'upper center'  : 9,
        'cente'         : 10
"""

plt.show()
