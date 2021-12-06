numbers = [2,3,1,5,4]
for j in range(0,len(numbers)-1):   #轮数
    for i in range(0,len(numbers)-1-j):
        if numbers[i] > numbers[i+1]:   #两两比较
            a = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = a
print(numbers)