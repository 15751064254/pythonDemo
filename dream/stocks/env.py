import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

stockFile = open('data_stocks.csv')
df = pd.read_csv(stockFile)
data = np.array(df['SP500'])
data = data[::-1]  # 反转,使数据按照日期先后顺序排序

plt.figure()
plt.plot(data)
plt.show()
