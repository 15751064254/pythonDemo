import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import data
data = pd.read_csv('data_stocks.csv')

# Dimensions of dataset
n = data.shape[0]
p = data.shape[1]

plt.plot(data['SP500'])
plt.show()
