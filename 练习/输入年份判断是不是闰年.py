year = int(input('请输入判断的年份：'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year}年是闰年')
else:
    print(f'{year}年不是闰年')