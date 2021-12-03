'''
模拟文件上传，键盘模拟输入上传文件名称，判断文件名是否大于6位以上，扩展名是否为：jpg,gif,png格式
如果不是则提示上传失败，如果名字不满足条件，而扩展名满足条件则随机生产一个6位数字组成的文件名，打印成功上传xxxxxx.png
'''
import random

filename = input('输入文件名：')
#判断文件名
if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.gif'):
    #判断文件名字
    i = filename.rfind('.')
    name = filename[:i] #切片
    #len(name)
    if len(name)<6:
        #重新构建名字
        n = random.randint(100000,999999)      #随机取名
        filename= str(n) + filename[i:]
    print('成功上传%s文件'%filename)
else:
    print('文件格式错误,上传失败！')

