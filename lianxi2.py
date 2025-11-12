# 定义四则运算函数
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b  # 若需处理除数为0，可增加异常判断

# 用字典映射操作编号与对应函数
op_dict = {
    '1': ('加', add),
    '2': ('减', sub),
    '3': ('乘', mul),
    '4': ('除', div)
}

print("请选择您需要的操作：1.加，2.减，3.乘，4.除")

# 获取输入
op = input("选择计算功能 (1,2,3,4)：")
num1 = float(input("输入num1:"))
num2 = float(input("输入num2:"))

# 通过字典get方法获取操作名称与函数，计算并格式化输出
op_name, op_func = op_dict.get(op, (None, None))
if op_func:
    result = op_func(num1, num2)
    print("{:.0f} {} {:.1f} = {:.1f}".format(num1, op_name, num2, result))
else:
    print("无效的操作编号")