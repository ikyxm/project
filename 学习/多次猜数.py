'''
产生随机数 random.randint(start,end)
可以猜多次，知道才对为止，如果猜错了适当给出提示，猜大了或着猜小了
'''
import random

computer = random.randint(1,50)
# print(computer)
#循环猜多次
while True:
    player = int(input('请输入您猜的数字:'))
    #猜错了，提示大小
    if player > computer:
        print('很遗憾，您猜大了！')
        continue
    if player < computer:
        print('很遗憾，您猜小了！')
        continue
    #猜对了，跳出循环
    player == computer
    print('恭喜您猜对啦')
    break
print('游戏结束！')