import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font',family='STXihei',size= 15)
df_wt = pd.read_csv('D:\\wps\\xuexi\\bz_df_wt.csv')
#读取第一个
df_wt1 = df_wt[df_wt['bin_bz_fs'] <= 20]
acwind = df_wt1['bin_bz_fs']
acpower = df_wt1['bin_bz_power']
#读取第二个表
df_g = pd.read_csv('D:\\wps\\xuexi\\bzglqx.csv', header=None)
df_g.columns = ['fs', 'gl']
g_w = df_g['fs']
g_p = df_g['gl']
plt.figure(figsize=(12,7))
plt.plot(acwind,acpower,label="实际功率曲线",color = 'b')
plt.plot(g_w,g_p,label="设计功率曲线",color = 'r')
plt.title("实测与设计功率曲线对比")
plt.xlabel('风速')
plt.ylabel('功率')
plt.legend()
plt.grid(color = '#95a5a6',linestyle='--',linewidth='3',axis='both',alpha=0.4)
plt.savefig("D:\\wps\\xuexi\\实测与设计功率曲线.png")
plt.show()