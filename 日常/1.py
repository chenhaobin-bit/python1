import random
def mingdan(team1,team2):
    zz = set(team1+team2)
    cc = list(zz)
    print("参与了大赛的同学有")
    paixu = sorted(cc,key=lambda x:ord(x[1]),reverse=False)
    print(paixu)
    zz = []
    xx = []
    std = ['小张','小李','小王','小赵','小孙','小周']
    for i in std:
        if i not in cc:
            zz.append(i)
    print("没参与大赛的同学有")
    paixu1 = sorted(zz,key=lambda x:ord(x[1]),reverse=False)
    print(paixu1)
    for i in std:
        if i in team1 and i in team2:
            xx.append(i)
    print("参加了两支队伍的同学有")
    paixu2 = sorted(xx,key=lambda x:ord(x[1]),reverse=False)
    print(paixu2)        
def main():
    std = ['小张','小李','小王','小赵','小孙','小周']
    seed = float(input('请输入随机种子'))
    print()
    random.seed((seed))
    team1 = random.sample(std,k = 3)
    team2 = random.sample(std,k = 3)
    print("大学生创新创业大赛队伍有")
    print(team1)
    print(team2)
    mingdan(team1,team2)
main()