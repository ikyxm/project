'''
删除：pop,remove,clear
pop(index)  根据下表删除列表中的元素，下标在写的时候要注意不要超出范围   index out of range
pop()   从后往前依次删除

remove(element)     根据元素名称进行删除  如果删除的元素列表中不存在则报错    list.remove(x): x not in list
如果列表中存在多个同名元素element,只删除遇到的第一个元素， 后面的元素不会被删除


关键字in   元素 in 列表    表示元素是否在列表中? 返回值:bool

clear()
'''

list1 = ['牛奶','面包','火腿','辣条']
#pop
# list1.pop(0)
# print(list1)

# list1.pop()
# print(list1)
# list1.pop()
# print(list1)

# #remove
# list1.remove('辣条')
# print(list1)

# list2 = ['牛奶','面包','火腿','辣条','牛奶']
# list2.remove('牛奶')
# print(list2)


#判断是否有存在的元素
# if '辣条呀' in list1:
#     print('存在')
# else:
#     print('不存在')

#删除多个元素
list2 = ['牛奶','牛奶','面包','火腿','辣条','牛奶']
# for i in list2:
#     if i == '牛奶':
#         list2.remove(i)
# print(list2)

# n = 0
# while n < len(list2):
#     if list2[n] == '牛奶':
#         list2.remove('牛奶')
#     else:
#         n += 1
# print(list2)

# print(list2.clear())

list3 = [1,2,3,4,5]
del list3[0]
print(list3)