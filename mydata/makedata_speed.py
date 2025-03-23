import numpy as np
import pandas as pd

# 读取CSV文件
data = pd.read_csv('PeMSD7_speed.csv', header=None)

# 将数据转换为NumPy数组
array = data.to_numpy()

# 添加一个维度
array = array.reshape((2880, 157, 1))

# 保存为nyz格式文件
np.savez('mydata.npz', array=array)