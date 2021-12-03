'''
替换内容: replace
replace(old,new,count)  默认全部替换，也可以通过count指定次数

切割字符串:split, rsplit, splitlines ,partition, rpartition
split('分隔符'，maxsplit)    从左向右分割，返回的结果是一个列表，maxsplit 最多的分割次数
rsplit('分隔符'，maxsplit)    从右向左分割，返回的结果是一个列表，maxsplit 最多的分割次数
splitlines  按行分割
partition('分隔符')   部分分割  分隔符左边，分隔符，分隔符右边

修改大小写: capitalize, title, upper, lower
'''

s = '萧炎'
result = s.replace('萧炎','岩枭')
print(result)

s = '萧炎 药老 美杜莎'
result = s.split(' ',1)
print(result)

s = '萧炎 药老 美杜莎'
result = s.rsplit(' ',1)
print(result)

s = '''萧炎
药老
美杜莎
'''
result = s.splitlines()
print(result)

s = '萧炎 药老 美杜莎'
result = s.partition(' ')
print(result)

s = 'hello world'
result = s.title()      #首字母大写
print(result)

s = 'hello world'
result = s.upper()      #全部字母大写
print(result)

s = 'HELLO WORLD'
result = s.lower()      #全部字母小写
print(result)

s = 'hello world'
result = s.capitalize()      #句首字母大写
print(result)