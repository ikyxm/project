'''
可变参数:
*args

拆包和封包
'''

#求和
# def get_sum(a,b):
#     sum = a + b
#     print(sum)
#
# get_sum(2,3)

def get_sum(*args):
    s = 0
    for i in args:
        s += i
    print('和是：',s)

get_sum(1,2,3)
get_sum(1,2,3,4,5)