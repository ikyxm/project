import random
n = 1
player_count = 0
computer_count = 0
while n <= 3:
    player = int(input("请输入（石头--0，剪刀--1，布--2）："))
    n += 1
    computer = random.randint(0, 2)
    if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        print("恭喜你赢了一局")
        player_count += 1
    elif player == computer:
        print("平局一局")
        player_count += 1
        computer_count += 1
    else:
        print("很遗憾输了一局")
        computer_count += 1
if player_count > computer_count:
    print('最终你赢啦！')
elif player_count == computer_count:
    print('最终平局啦!')
else:
    print('最终你输啦！')