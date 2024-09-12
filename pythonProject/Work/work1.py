#编写程序，输入一个任意大自然数，输出各位数字之和
def sum_of_digits(n):
    # 将输入的自然数转换为字符串
    str_n = str(n)
    # 初始化总和为0
    total_sum = 0
    # 遍历字符串中的每一个字符
    for char in str_n:
        # 将字符转换为数字并累加到总和中
        total_sum += int(char)
    # 返回总和
    return total_sum

# 示例：输入一个自然数
number = input("请输入一个自然数：")
# 计算各位数字之和
result = sum_of_digits(number)
# 输出结果
print(f"数字 {number} 的各位数字之和是 {result}")
