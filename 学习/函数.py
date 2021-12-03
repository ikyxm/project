'''
函数
格式：
def 函数名([参数...])
    代码

函数名:    get_name()
          search()
代码:
        封装重复内容
'''
import random


def generate_code():
    #生成验证码
    s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    code = ''
    for i in range(4):
        r = random.choice(s)
        code += r
    print(code)

#调用函数
generate_code()



