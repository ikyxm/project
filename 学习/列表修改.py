'''
修改:
[1,2,3,4,5,6]
insert(位置,元素):元素占了位置，其他元素只能向后移动
index(元素):根据元素找该元素的位置下标，返回值是下标位置
'''

list1 = [1,2,3,4,5,6]

# list1.insert(1,8)
# print(list1)

list1[0] = 8
print(list1)

weizhi = list1.index(5)

list1[weizhi] = 8
print(list1)