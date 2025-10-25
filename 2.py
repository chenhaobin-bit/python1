class Calculator:
    data = []
    def __init__(self,nums):
        if nums is not None:
            self.data = nums
            Calculator.data = nums
    def instance_sum(self):
        return sum(self.data)
    @classmethod
    def sum(cls):
        return sum(cls.data)
    
nums = eval(input())
sum1 = Calculator(nums)
print(sum1.data)
print(sum1.instance_sum())
print(Calculator.sum())