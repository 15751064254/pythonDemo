import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000), index = np.arange(1000))
data.cumsum()
data.plot()
plt.show()
