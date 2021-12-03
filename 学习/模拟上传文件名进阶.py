'''
模拟文件上传，键盘模拟输入上传文件名称，判断文件名是否大于6位以上，扩展名是否为：jpg,gif,png格式
如果不是则提示上传失败，如果名字不满足条件，而扩展名满足条件则随机生产一个6位字母数字组成的文件名，打印成功上传xxxxxx.png
'''
import random

filename = input('请输入上传的文件名：')
#判断文件类型
if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.gif'):    #判断文件类型
    i = filename.find('.')      #以.切片
    front = filename[:i]        #分割文件名
    if len(front)<6:    #如果文件名小于6位
        front = ''
        s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
        for a in range(6):
            index = random.randint(0,len(s)-1)      #随机产生下标
            front += s[index]       #下标匹配字母
    filename = front + filename[i:]
    print('上传%s成功！'%filename)
else:
    print('格式错误，请重新上传!')