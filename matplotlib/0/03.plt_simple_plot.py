# 3 - simple plot

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2*x + 1
# y = x**2
plt.plot(x, y)
plt.show()

# Terminal: export DISPLAY=:0;python3 03.plt_simple_plot.py
