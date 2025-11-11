import pandas as pd
import numpy as np
def pandaun(series):
    return series.max() - series.min()
df = pd.read_csv("D:\\wps\\xuexi\\flight.csv")
df3 = df[(df['dist'] > 1000) & (df['dist'] < 1200)]
df4 = df[df['time'] > 100]
df5 = pd.concat([df3,df4],axis=0);
df6 = df3[['time','dist']]
dest_count = df.groupby('dest')['dest'].agg(np.size).rename('dest_count')
df7 = dest_count.reset_index()[['dest','dest_count']]
print(df7)
df5.to_csv("D:\\wps\\xuexi\\df5.csv")
df7.to_csv("D:\\wps\\xuexi\\df7.csv")