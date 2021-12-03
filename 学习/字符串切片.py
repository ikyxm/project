s = 'ABCDEFG'
#字符串索引
#print(s[0])
'''
切片：字符串,列表
格式：字符串变量[start:end]  #end取不到
字符串变量[start:end:step]   默认是从左到右一个一个取元素
step:
1.步长
2.方向     step 正数 从左到右
          step 负数 从右到左
'''
#print(s[0:1])
#取BCD
print(s[1:4])
print(s[0:4:2])
print(s[::-1])

