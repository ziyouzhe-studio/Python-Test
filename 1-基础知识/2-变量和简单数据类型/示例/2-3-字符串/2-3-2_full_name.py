# 在字符串中使用变量
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # f(format, 设置格式)，把花括号内的变量转换为其值(字符串)
print(full_name)
print(f"Hello, {full_name.title()}")
message = f"Hello, {full_name.title()}" # 使用f字符串创建消息，赋值给变量
print(message)