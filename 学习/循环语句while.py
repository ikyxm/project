'''

while 条件:
    要循环执行的代码

'''

'''
#初始值
n = 1
#结束条件
while n <= 10:
    print('n = %d' %n)
    n += 1
'''

# 1.打印1-50之间能被3整除的数字
# 2.打印1-10之间数字的累加和
# 1.
'''
n = 1
while n <= 50:
    if n%3 == 0 :
        print('n = %d' %n)
    n += 1
'''
# 2.
n = 1
sum = 0 #容器 存放和的结果
while n <= 10 :
    sum += n    #sum = sum + n
    n += 1      #n = n + 1
print('累加和sum=',sum)

'''
sum = 0    sum = 1
n = 1       n = 2
sum = 1     sum = 3
n = 2       n = 3
'''