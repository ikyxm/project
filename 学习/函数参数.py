'''
参数:
    1.无参数.
    2.有参数
无参数:
    def函数名():
        pass
有参数:
    def函数名([参数1,参数2,参数3......]):
        pass
参数就是在调用函数时向函数中传值作用

'''
import random


def generate_code(n):
    #生成验证码
    s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    code = ''
    for i in range(n):
        r = random.choice(s)
        code += r
    print(code)

#调用函数
generate_code(4)

generate_code(6)

