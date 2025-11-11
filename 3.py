class Zoo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def feed(self):
        print(f"{self.name}正在被喂食")
class Lion(Zoo):
    def make_sound(self):
        print(f"{self.name}发出了咆哮声")
class ee(Zoo):
    def make_sound(self):
        print(f"{self.name}发出了喇叭声")

xx = Zoo("辛巴","5")
qq = ee("小飞象","8")
xx.make_sound()
xx.feed()
qq.make_sound()
qq.feed()