import random
computer = random.randint(0,50)
count = 0
while True:
    player = int(input('猜一个1-50的数：'))
    count += 1
    if player == computer:
        if count == 1:
            print('赶快去买彩票去吧，运气爆了！')
        elif 2 <= count <= 5:
            print('猜对了，运气还可以哦！')
        elif count >= 6:
            print('猜对了，运气一般啊')
        break
    elif player >= computer:
        print('猜大了，猜小一点!')
    else:
        print('猜小了，猜大一点！')
