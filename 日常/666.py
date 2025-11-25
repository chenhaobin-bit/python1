import pandas as pd
import numpy as np
df = pd.read_csv("D:\\wps\\xuexi\\flight.csv")
df['low_dest'] = df['dest'].str.lower()
print("添加后的文件为")
print(df)
df3 = df[(df['dist'] > 1000) & (df['dist'] < 1200)]
print(df3)
df4 = df[df['time'] > 100]
print(df4)
df5 = pd.concat([df3,df4],axis=0);
print(df5)
df6 = df3[['time','dist']]
print(df6)
diff = df6.apply(lambda col: col.max() - col.min())
print("df6每列最大值与最小值的差值：")
print(diff)