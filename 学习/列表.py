# shoppingcar = []
# while True:
#     name = input('商品名：')
#     price = input('价格：')
#     numbe = input('数量：')
# print('清单')

'''
如何定义一个列表：
1.空列表：[]
2.有内容的列表：['A','B','C'],[1,2,3,4]
'''

list1 = []
print(type(list1))

#获取列表里面的元素,通过索引（下标）
list2 = ['牛奶','面包','辣条','臭豆腐']
print(list2[2])

#切片
print(list2[0:2])
print(list2[::-2])
print(list2[::-1])