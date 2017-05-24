import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.DataFrame(
np.random.randn(100,4),
index = np.arange(100),
columns = list("ABCD"))

print(data)
data.cumsum()
data.plot()
plt.show()
