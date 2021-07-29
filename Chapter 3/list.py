# 什么是列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'java']
print(bicycles)

# 访问列表元素
print(bicycles[0])  # 列表中元素序号从0开始计数
print(bicycles[0].title())

# 索引从0开始而不是1开始
print(bicycles[1])
print(bicycles[3])

# 负数索引：常用在不知道列表长度的情况下
print(bicycles[-1])

# 使用列表中的各个值
message = 'My first bicycle was a ' + bicycles[-1].title() + '.'
print(message)

# 练习3-1
name = ['何嘉琛', '胡旭辰', '马添', '卢树人']
print(name[0])
print(name[1])
print(name[-2])
print(name[-1])

# 练习3-2
message = name[0] + ' , 早上好啊！'
print(message)

# 练习3-3
transportation=['car','bus','taxi','bike','walk']
print('I would like to own a '+transportation[-2].title())
