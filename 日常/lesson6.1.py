import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = "SimHei"
df = pd.read_csv("D:\\wps\\xuexi\\scmd_CalculationData.csv")
wind1 = df['winddirection']
wind2 = df['windspeed1']
plt.figure(figsize=(10,6))
plt.scatter(wind1,wind2,color="blue",s=1,alpha=0.6)
plt.title("风速与风向的函数")
plt.xlabel("风向")
plt.ylabel("风速")
plt.grid(True)
plt.savefig('D:\\wps\\xuexi\\风速与风向的函数.png')
plt.show()