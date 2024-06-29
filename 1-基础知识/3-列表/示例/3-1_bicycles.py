# 列表由一系列按特定顺序排列的元素组成。
# 列表使用[]表示，并用逗号分隔其中的元素。
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # 列表是有序集合，告诉列表索引从0开始，并将其放在列表后面括号内。访问最后一个元素，指定索引为-1。

# 使用列表中的各个值。
# 使用f字符串根据列表中的值创建消息
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)