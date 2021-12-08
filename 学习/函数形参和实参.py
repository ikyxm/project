'''
函数的形参和实参
'''

#定义一个函数
def say_hi(name):  #形参
    print('Hello',name)

say_hi('tom')   #实参
say_hi('jack')

def my_sum(a,b):
    print(a+b)

my_sum(1,2)
# my_sum(1)   my_sum() missing 1 required positional argument: 'b'
# my_sum(1,2,3)  my_sum() takes 2 positional arguments but 3 were given