'''
sort
reverse

'''

#生成8个1-20之间的随机数，保存在列表中，遍历打印
import random

numbers = []
for i in range(8):
    ran =random.randint(1,20)
    numbers.append(ran)

print(numbers)

numbers.reverse()
print(numbers)  #没有排序，翻转

# numbers.sort()    #默认升序，通过reverse参数控制升序还是降序   True 降序 False 升序 默认
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

