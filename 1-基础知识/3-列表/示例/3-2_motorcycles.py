# 修改，添加和删除元素
# 3.2.1修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

# 3.2.2在列表中添加新元素
# motorcycles.append('ducati') # 最简单的方式就是.append(), 直接在列表末尾添加新元素
# print(motorcycles)

# 使用方法insert()在列表任意位置添加新元素
# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# 3.2.3 从列表中删除元素
# 使用del语句删除元素
# del motorcycles[0]
# print(motorcycles)

# 使用pop()删除元素
# pop()方法删除列表元素，并能够接着使用它的值
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# 根据值删除元素
# 如果你只知道元素的值，不知到元素索引，可以使用方法remove()。
# motorcycles.remove('suzuki')
# print(motorcycles)

# 使用remove()删除元素后，依然可以使用它的值
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")