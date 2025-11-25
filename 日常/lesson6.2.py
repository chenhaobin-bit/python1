import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = "SimHei"
cf = pd.read_csv("D:\\wps\\xuexi\\scmd_CalculationData.csv")
fields = ['windspeed1', 'power_max', 'power_min', 'power', 'power_dev']
data=cf[fields]
plt.figure(figsize=(10, 6))
plt.scatter(data['windspeed1'], data['power_max'], label='power_max', marker='o')
plt.scatter(data['windspeed1'], data['power_min'], label='power_min', marker='s')
plt.scatter(data['windspeed1'], data['power'], label='power', marker='^')
plt.scatter(data['windspeed1'], data['power_dev'], label='power_dev', marker='v')
plt.title('功率特性散点图')
plt.xlabel('风速(windspeed1)')
plt.ylabel('功率')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("D:\\wps\\xuexi\\2功率特性散点图.png")