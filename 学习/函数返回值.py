'''
参数：外界向里面传值
返回值：里面的内容向外界传送

def 函数名(参数...):
    ...
    ...
    return  xxxx
当函数调用时通过return向外返回值
注意：只要函数有返回值，则需要接收
'''
def get_sum(*args):
    total = 0
    for i in args:
        total += i
    print('内部:',total)
    #将total返回
    return  total

t = get_sum(1,2,3)
print('外侧：',t)
x = 100
x = x + t
print(x)