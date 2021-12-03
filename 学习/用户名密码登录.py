'''
用户名或者手机号登录+密码
用户名：全部小写，首字母不能是数字，长度必须是6位以上
手机号码：纯数字 长度11位、
密码：必须是6位数字  输入多次，但是次数不能超过3次

以上符合条件则进入下层验证：
判断用户名+密码 是否正确，则成功，否则登录失败
'''
login = True
count = 0
while login:
    username = input('请输入您的用户名或者手机号：')
    if (username.islower() and username[0].isalpha() and len(username) >= 6) or (username.isdigit() and len(username) == 11):
        print(username)
        while True:
            password = input('请输入您的密码：')
            count += 1
            if count >= 3:
                print('密码多次输入错误，账号已被锁定！')
                login = False
                break
            if password.isdigit() and len(password) == 6:
                if username == 'adminyikm' or 'username == 18727916715' and password == '002113':
                    print('登录成功！')
                    login = False
                    break
            else:
                print('密码错误，请重新输入！')
    else:
        print('用户名或手机号错误，请重新登录！')
