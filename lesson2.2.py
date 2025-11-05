import pandas as pd
df = pd.read_csv("D:\\wps\\xuexi\\flight.csv")
df1 = df[['date','dist','flight']]
df2 = df.iloc[[3,4],[0,1]]
print("df1为")
print(df1)
print("df2为")
print(df2)
df['low_dest'] = df['dest'].str.lower()
print("添加后的文件为")
print(df)
