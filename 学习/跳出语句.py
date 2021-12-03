'''
break
continue

都是在循环中。

不同：
break 跳出循环结构
contin 跳出本次循环，继续下一次循环
'''
#不打印被3整除的
# for i in  range(10):
#     if i%3!=0:
#         print(i)

for i in range(10):
    if i % 3 == 0:
        continue
        #break
    print(i)