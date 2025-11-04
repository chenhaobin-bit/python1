import pandas as pd
import numpy as np
# # 创建Series​
s = pd.Series([1,3,5,np.nan,6,8])
# #print(s)
# # 带索引的Series​
# z = pd.Series([1,3,5],index = ['a','b','c'])
# #print(z)
# # 从字典创建DataFrame
data = {
    '姓名': ['张三', '李四', '王五', '赵六',np.nan,'赵六'],
    '年龄': [25, 30, 35, 40,np.nan,40],
    '城市': ['北京', '上海', '广州', '深圳',np.nan,'深圳'],
    '薪资': [8000, 12000, 15000, 18000,np.nan,18000]
}
df = pd.DataFrame(data)
# #查看基本信息
# print(df.info())
# #查看数据描述统计
# print(df.describe())
# #查看索引和列名
# print(df.columns)
# print(df.index)
# #查看数据
# print(data)
# # 查看数据类型
# print(df.dtypes)
# # 转换数据类型
# df['薪资'] = df['薪资'].astype(float)
#处理缺失值
df.dropna()
zzz = df.fillna({"姓名":'田武',"年龄": 99,"城市":'炮国',"薪资":666})
#print(zzz)
# and 重复值 
cc = zzz.drop_duplicates()
#print(cc)
# and 条件筛选
gj = cc[cc["薪资"] > 666]
#print(gj)
# 按列计算均值，求和，最值
print(cc['薪资'].mean())
print(cc["年龄"].sum())
print(cc['薪资'].max())
# 3. 数据排序（按工资降序排列）
df_sorted = cc.sort_values(by="薪资", ascending=False)
print(df_sorted)