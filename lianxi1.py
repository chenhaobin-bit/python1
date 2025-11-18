# def jj(n):
#     if(n == 0):
#         return 1
#     return jj(n-1)*n
# def main():
#     n = int(input())
#     print(jj(n))
# main()
# # 创建初始字典
# en_zh = {'apple': '苹果', 'banana': '香蕉'}

# # 添加3个新键值对
# en_zh['cat'] = '猫'
# en_zh['dog'] = '狗'
# en_zh['egg'] = '鸡蛋'

# # 删除键'banana'
# del en_zh['banana']
# # for i, j in enumerate(en_zh):
#     print(i,j)
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
# match(en_zh['apple']):
#     case "苹果":
#         print("yes")

# user = int(input())
# if user == 2:
#     print(True)
# elif user <= 1:
#     print(False)
# else:
#     is_prime = True
#     for i in range(2, user):
#         if user % i == 0:
#             is_prime = False
#             break
#     print(is_prime)
# class Zoo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def feed(self):
#         print(f"{self.name}正在被喂食")
# class Lion(Zoo):
#     def make_sound(self):
#         print(f"{self.name}发出了咆哮声")
# class ee(Zoo):
#     def make_sound(self):
#         print(f"{self.name}发出了喇叭声")

# xx = Lion("辛巴","5")
# qq = ee("小飞象","8")
# xx.make_sound()
# xx.feed()
# xx.feed()
# qq.make_sound()
# qq.feed()
# class Student:
#     count = 0
#     def __init__(self,name,sex):
#         self.name = name
#         self.sex = sex
#         Student.count += 1
#     def add(self, name,sex):
#         self.name = name
#         self.sex = sex
#         Student.count += 1
# stu1 = Student("dd",11)
# stu2 = Student("ss",12)
# print("stu1学生姓名：%s,性别：%s,数量信息：%d"%(stu1.name,stu1.sex,Student.count))
# print("stu2学生姓名：%s,性别：%s,数量信息：%d"%(stu2.name,stu2.sex,Student.count))
# # class Calculator:
# #     data = []
# #     def __init__(self,nums):
# #         if nums is not None:
# #             self.data = nums
# #             Calculator.data = nums
# #     def instance_sum(self):
# #         return sum(self.data)
# #     @classmethod
# #     def sums(cls):
# #         return sum(cls.data)
    
# # nums = eval(input())
# # sum1 = Calculator(nums)
# # print(sum1.data)
# # print(sum1.instance_sum())
# # print(Calculator.sums())
# def main():
#     dd = {"羽毛球":4,"武术":3,"舞蹈":2,"绘画":1}
#     dd1 = dict(sorted(dd.items(),key=lambda x:x[1],reverse=True))
#     for i,j in enumerate(dd1):
#         print(f"{i}：{j}")
# main()