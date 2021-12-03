'''
模拟论坛
'''
msg = input('发表一句话：')
print('-'*50)
print('以下为回复内容：')
login = True
while login:
    #输入用户名
    username = input('请输入您的用户名：')
    while True:
        #输入回复内容
        reply = input('评论：')
        reply = reply.strip()   #剔除空格
        #验证内容
        if len(reply)!=0:
            #验证长度是否超过20字
            if len(reply)<=20:
                #是否存在敏感词汇
                reply = reply.replace('傻逼','**')
                print('\t{}发表的评论是：\n\t{}'.format(username,reply))
                login = False
                break
            else:
                print('不能超出20字！')
        else:
            print('评论为空，请重新输入评论')
        #成功发表评论，否则重新输入