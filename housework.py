import numpy as np
arr1 = np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr1)
#输出维度
print(arr1.ndim)
#输出形状
print(arr1.shape)
#创建数组
arr2 = np.zeros((2,2)) #全为零的数组
arr3 = np.ones((2,2))  #全为一的数组
arr4 = np.arange(12)    #生成顺序数组
