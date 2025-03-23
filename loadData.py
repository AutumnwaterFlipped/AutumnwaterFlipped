import matplotlib.pyplot as plt
import numpy as np

pems04_data = np.load('./data/PEMS04/pems04.npz')

# print(pems04_data.files)
#
# print(pems04_data['data'].shape)
# (16992, 307, 3)
# 16992=59天*24小时*12
# 特征：交通流量，平均速度，平均占用率
flow = pems04_data['data'][:,0,0]
speed = pems04_data['data'][:,0,0]
occupy = pems04_data['data'][:,0,0]
fig = plt.Figure(figsize=(15,5))
plt.title('traffic flow in San Francisco')
plt.xlabel('day')
plt.ylabel('flow')
plt.plot(np.arange(len(flow)),flow,linestyle='-')
plt.plot(np.arange(len(flow)),speed,linestyle='-')
plt.plot(np.arange(len(flow)),occupy,linestyle='-')
fig.autofmt_xdate(rotation=45)
file_data = np.load('./data/PEMS04/pems04_r1_d1_w1_astcgn.npz')
print(file_data.files)
# import numpy as np
# file_path="D:\Python\project\ASTGCN-pytorch-master\data\PEMS04\pems04.npz"
# data=np.load(file_path,allow_pickle=True)
# data = np.load(file_path)
# print(data.files)
# print(data['data'])




