'''
空格处理:ljust, rjust, center, lstrip, rstrip, strip
字符串拼接:join
'''
username = 'admin '
print(len(username))

# username = input('用户名：')
# print(len(username))

s = '  admin  '
print(len(s))
result = s.strip()      #剔除左右两侧空格
print(result)
print(len(result))

s = '  admin  '
print(len(s))
result = s.lstrip()      #剔除左侧空格
print(result)
print(len(result))

s = '  admin  '
print(len(s))
result = s.rstrip()      #剔除右侧空格
print(result)
print(len(result))

s = 'hello world'
result = s.center(30)       #给定30个字符，将字符放在中央位置
print(result)
print(len(result))

result = s.ljust(30)         #给定30个字符，将字符放在左侧位置
print(result)
print(len(result))

result = s.rjust(30)         #给定30个字符，将字符放在右侧位置
print(result)
print(len(result))