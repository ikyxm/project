'''
生成8个1-100之间的随机整数，保存到列表中
键盘输入一个1-100之间的整数，将整数插入到排序后的列表中（升序降序没有要求）
[1,9,6,8,3]
[1,3,6,8,9]
5
[1,3,5,6,8,9]
'''
import random

numbers = []
for i in range(8):
    ran = random.randint(1,100)
    numbers.append(ran)
# print(numbers)
numbers.sort()
# print(numbers)
num = int(input('请输入一个1-100的整数：'))
numbers.append(num)
numbers.sort()
print(numbers)