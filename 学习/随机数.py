import random
number = random.randint(1,10)
print(number)
guess = input('请输入你猜的数字(1-10)：')

if int(guess) == number: #类型要一致，input默认为str
    print('恭喜你猜对了！')