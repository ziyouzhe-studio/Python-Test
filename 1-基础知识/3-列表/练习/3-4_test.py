# 嘉宾名单
# 创建一个列表名单，邀请至少三人，然后打印消息
name_list = ['tall', 'alexandria', 'rose', 'clara']

# print(f"welcome to my party, {name_list}")

# 修改嘉宾名单。嘉宾无法赴约，邀请另一位嘉宾。
# 指出哪一位嘉宾无法赴约
# 修改嘉宾名单，将无法赴约的嘉宾名字更换为新嘉宾的名字
# 再次打印消息，邀请每一位嘉宾
# test_1 = name_list.pop(2)
# print(test_1)
# print(f"The guest is unable to attend the appointment, {test_1.title()}")

# name_list.append('cook')
# print(name_list)

# print(f"welcome to my party, {name_list}")

# 3-6 添加嘉宾
# 找到了更大的餐桌，可以容纳更多的顾客，邀请至少三名新顾客。
# 以3-4和3-5为基础上，在程序末尾添加一条语句，指出你找到了更大的餐桌。

name_list.insert(0, 'alice')
# name_list.insert(3, 'james')
name_list.append('franklin')
# print(name_list)

# print(f"hello everyone welcome to my party, {name_list}")

# 3-7 缩减名单
# 只能邀请两名嘉宾
# 以3-6为基础，在程序末尾添加一段代码，打印只能邀请两名嘉宾进行晚餐的消息。
print("Sorry, only two guests can be invited for this dinner")
# 只有pop()删除嘉宾，只剩两名。将每次被删除的嘉宾都打印一条消息。
test_name_1 = name_list.pop(0)
print(f"Sorry, {test_name_1.title()}")

test_name_2 = name_list.pop(1)
print(f"Sorry, {test_name_2.title()}")

test_name_3 = name_list.pop(2)
print(f"Sorry, {test_name_3.title()}")

# test_name_4 = name_list.pop(3)
# print(f"Sorry, {test_name_4.title()}")


# print(name_list)

del name_list[0]
del name_list[1]
# del name_list[2]

print(name_list)