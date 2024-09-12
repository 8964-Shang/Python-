#编写程序，输入一个自然数，输出它对应的二进制，八进制和十六进制表示形式（建议使用多种print函数格式）
number = int(input("请输入一个自然数："))
print("二进制表示形式：",bin(number))
print("八进制表示形式：",oct(number))
print("十六进制表示形式：",hex(number))
