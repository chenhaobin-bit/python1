import matplotlib.pyplot as plt
import numpy as np
# fig = plt.figure(figsize = (10,6))
# plt.axes()#默认坐标轴
# plt.subplot(2,2,4)#两行两列，第四个位置
# plt.subplot(2,2,1)
fih,axarr = plt.subplots(2,2,figsize = (10,6))#默认创建一个2行2列的坐标系
x = np.linspace(0,6,100)
y = np.sin(2*np.pi*x)
# axarr[0,0].plot(x,y,color = 'r',linewidth = 3,linestyle = '-')
# axarr[0,1].plot(x,y,color = 'b',linewidth = 3,linestyle = ':')
# axarr[1,0].plot(x,y,color = 'r',linewidth = 3,linestyle = '-')
# axarr[1,1].plot(x,y,color = 'b',linewidth = 3,linestyle = ':')
axarr[0,0].plot(x,y,color = 'r',linewidth = 1,linestyle = '-',marker='o')#marker 代表用什么标记某个点
axarr[0,1].plot(x,y,color = 'g',linewidth = 1,linestyle = ':',marker='s')
axarr[1,0].plot(x,y,color = 'b',linewidth = 1,linestyle = '-',marker='^')
axarr[1,1].plot(x,y,color = 'y',linewidth = 1,linestyle = ':',marker='+')
plt.title("cs")
# plt.plot(x,y,color = 'r',linewidth=3,linestyle='-')
plt.show()
