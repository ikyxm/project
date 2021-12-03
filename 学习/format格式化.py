'''
格式化：
1.%d %s %f ......
print(‘我叫%s!' % name)
2.format
'''

name = '萧炎'
age = '18'

result = '天才少年{},今年{}岁'.format(name,age)
print(result)

#数字字段名
result = '天才少年{0},今年{1}岁,我也是{1}岁！'.format(name,age)
print(result)

#变量字段名
s = '{name}本次考试平均分为：{math}，语文分数：{chinese}，数学分数：{math}，英语分数：{english}'.format(name='jack',chinese=99,math=100,english=101)
print(s)