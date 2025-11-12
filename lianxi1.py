# def jj(n):
#     if(n == 0):
#         return 1
#     return jj(n-1)*n
# def main():
#     n = int(input())
#     print(jj(n))
# main()
# 创建初始字典
en_zh = {'apple': '苹果', 'banana': '香蕉'}

# 添加3个新键值对
en_zh['cat'] = '猫'
en_zh['dog'] = '狗'
en_zh['egg'] = '鸡蛋'

# 删除键'banana'
del en_zh['banana']
for i, j in enumerate(en_zh):
    print(i,j)
# class Person:
#     country = "中国"
#     def __init__(self,name,age,scores,password):
#         self.name = name
#         self.age = age
#         self.socres = scores
#         self.__password = password
#     def avg_score(self):
#         top3 = self.socres[:3]
#         return sum(top3) / len(top3)
#     @staticmethod
#     def welcome():
#         print("欢迎！")
# p1 = Person("张三",18,[22,33,22,33,11],"123456")
# p1.welcome()
# print(f"国家{p1.country}")
# print(f"姓名：{p1.age}")
# print(f"平均分：{p1.avg_score():.0f}")