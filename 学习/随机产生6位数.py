# 字母和数字组合
import random

filename = ''
s = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
for i in range(6):      #取6个字符
    index = random.randint(0,len(s)-1)  #随机产生下标    步长-1相对于切片中的下标
    filename += s[index]    #获得下标匹配字母
print(filename)     #随机生成6位作为文件名