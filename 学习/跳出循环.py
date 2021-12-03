# count = 0
# while True:
#     print('------')
#     count += 1
#     if count == 5:
#         break   #跳出循环结构

total = 0
numberadd = 0
while True:
    #购买
    price = float(input('请输入价格:'))
    number = int(input('请输入数量:'))
    #总价
    total += price*number
    #总数
    numberadd += number
    print('-----')
    #判断是否购买
    answer = input('当前商品总额是：%.2f，是否继续添加商品？（q表示退出）'%total)
    if answer == 'q':
        break
print('您一共购买的商品数量为:%d,所有的商品总额是:%.2f' %(numberadd,total))