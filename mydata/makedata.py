import pandas as pd

# 读取CSV文件
df = pd.read_csv("newData_distance.csv")

# 将 "from" 和 "to" 列中的数字减一
df['from'] = df['from'] - 1
df['to'] = df['to'] - 1


# 保存修改后的数据到新的CSV文件
df.to_csv("newData_distance.csv", index=False)
