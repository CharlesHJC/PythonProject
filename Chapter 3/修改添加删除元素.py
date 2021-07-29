# 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 添加列表元素
motorcycles.append('honda')  # 在列表末尾添加新元素
print(motorcycles)

motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 在列表中插入元素
motorcycles.insert(1, 'ducati')  # 选择插入元素的位置
print(motorcycles)

# 删除列表元素
# del方法
motorcycles = ['honda', 'ducati', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# pop方法
motorcycles = ['honda', 'ducati', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)  # 被删除的值存储在popped_motorcycle中，依然可以访问

last_owned = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owned.title() + '.')

# 弹出列表中任何位置处的元素
first_owned = motorcycles.pop(1)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# 根据值删除元素
motorcycles = ['honda', 'ducati', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

# 指出删除原因
motorcycles = ['honda', 'ducati', 'yamaha', 'suzuki']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')

# remove()只能删除第一个指定的值。


# 练习3-4
# 嘉宾名单
guest = ['胡旭辰', '马添', '卢树人']  # 客人名单
invitation = '诚挚的邀请：' + guest[0] + ' 参加我的生日晚宴。'
print(invitation)
invitation = '诚挚的邀请：' + guest[1] + ' 参加我的生日晚宴。'
print(invitation)
invitation = '诚挚的邀请：' + guest[2] + ' 参加我的生日晚宴。'
print(invitation)

# 简单算法
guest = ['胡旭辰', '马添', '卢树人']  # 客人名单
x = 0
while x < 3:
    invitation = '诚挚的邀请：' + guest[x] + ' 参加我的生日晚宴。'
    x = x + 1
    print(invitation)

# 练习3-5
# 修改嘉宾名单
print('无法赴约的嘉宾: ' + guest[-1])
guest[-1] = '吕涵琪'
x = 0
while x < 3:
    invitation = '诚挚的邀请：' + guest[x] + ' 参加我的生日晚宴。'
    x = x + 1
    print(invitation)

# 练习3-6
# 增加嘉宾
print('因为没有小的包间了，所以换成了大包间，邀请了我女朋友的弟弟妹妹')
guest.insert(0, '夏时雨')
guest.insert(2, '焦博研')
guest.append('张星')
print(guest)  # 嘉宾名单
x = 0
while x <= 5:
    invitation = '诚挚的邀请：' + guest[x] + ' 参加我的生日晚宴。'
    x = x + 1
    print(invitation)

# 练习3-7
# 缩减名单
print(guest)
x = 5
while x >= 2:
    x = x - 1
    guest.pop()
    apologize = '非常抱歉： ' + guest[x] + ' 因为一些特殊原因，无法邀请您来共进晚餐。'
    print(apologize)
print(guest)
while x >= 0:
    x = x - 1
    invitation = '诚挚的邀请：' + guest[x] + ' 参加我的生日晚宴。'
    print(invitation)
del guest[0:2]
print(guest)
