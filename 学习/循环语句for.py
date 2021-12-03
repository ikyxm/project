'''
格式：
for i in range(n):
    循环体中的内容

range(n): 从0开始取值到n-1结束
range(start,end): [start,end) 左闭右开
range(start,end,step): 从start开始（包含）到stop结束（不包含），其中步长为step，默认为1
'''

#1-10 数字打印
# for i in range(10):
#     print(i+1)

# for i in range(1,11):
#     print(i)

# for i in range(1,11,2):
#     print(i)

#1-50累加和for循环

# sum = 0
# for i in range(1,51):
#     sum += i    # sum = sum + i
# print(sum

#最多属于用户名和密码三次，如果三次没有登录成功，提示账号被锁定
#break退出
# for i in range(3):
#     #提示输入用户名和密码
#     username = input('用户名:')
#     passwd = input('密码:')
#     #判断输入密码是否正确 admin 123456
#     if username == 'admin' and passwd == '123456':
#         print('用户登录成功！')
#         break
#     print('用户名或者密码错误！\n')
# if i == 2:
#     print('三次没有登录成功，账号已被锁定！')
'''
for i in range(n):
    循环体中的内容
else:
    如果上面的for0~n-1循环没有出现中断（break）
    
while......else
for......else
注意else不被中断才会执行
'''
for i in range(3):
    #提示输入用户名和密码
    username = input('用户名:')
    passwd = input('密码:')
    #判断输入密码是否正确 admin 123456
    if username == 'admin' and passwd == '123456':
        print('用户登录成功！')
        break
    print('用户名或者密码错误！\n')
else:
    print('三次没有登录成功，账号已被锁定！')