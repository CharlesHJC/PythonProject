# 例子
print('I told my friend, "python is my favorite language"')

# 字符串大小写
name = 'hejiachen'
print(name.title())
print(name.upper())
print(name.lower())

# 合并拼接字符串
first_name = 'He'
last_name = 'jiachen'
full_name = first_name + ' ' + last_name
print(full_name)

message = 'HELLO ' + full_name + '!'
print(message)

# 制表符、换行符
print('python')
print('\tpython')
print('Languages:\npython\nC\nJava')
print('Languages:\n\tpython\n\tC\n\tJava')

# 删除空白
favorit_language = '   python   '
print(favorit_language)
print(favorit_language.lstrip())
print(favorit_language.rstrip())
# 删除空白并替换数据
favorit_language = favorit_language.strip()
print(favorit_language)

# 字符串语法错误
# message='One of Python's strengths is its diverse community'    # 单引号报错

message = "One of Python's strengths is its diverse community"  # 双引号不报错
print(message)

# Python2中 打印内容无需放在括号内 因为Python3中的print是一个函数，所以括号必不可少
# print 'Hello Python2.7 world'       #这里报错是因为目前的解释器为Python3.8



# 练习2-3
name = 'Hejiachen'
print('Hello ' + name + ',would you like to learn some Python today?')

# 练习2-4
name = 'hejiachen'
print(name.upper())
print(name.lower())
print(name.title())

# 练习2-5
print("Steve Jobs said, 'We're here to put a dent in the universe!'")

# 练习2-6
famous_person = 'Steve Jobs'
dictum = "'We're here to put a dent in the universe!'"
message=famous_person+' said, '+dictum
print(message)

# 练习2-7
name=' \n  hejiachen  \t '
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())



