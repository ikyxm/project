'''
只要字符串可以调用
判断：startswith,endswith,isalpha,isdigit,isalnum,isspace
返回的都是布尔型
'''

m = 'https://www.baidu.com/s'
result = m.startswith('http')   # 判断是否以xxx开头的
print(result)

n = 'xxx.jpg'
result = n.endswith('MP4')  # 判断是否以xxx结尾的
print(result)

a = 'A1234'
result = a.isalpha()    #判断是否全部是字母
print(result)

b = '123456'           #判断是否全部是数字
result = b.isdigit()
print(result)

c = 'A1234'             #判断是否全部是数字和字母
result = c.isalnum()
print(result)

d = 'ABCD'
result = d.isupper()       #判断是否全部是大写字母
print(result)

e = 'abcd'
result = e.islower()        #判断是否全部是小写字母
print(result)

space = '    '          #判断是否全部是空格
result = space.isspace()
print(result)