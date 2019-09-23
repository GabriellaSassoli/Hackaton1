
numbers = range(20,1000000000,20)
print(numbers)
for i in numbers:
    num = []
    for j in range(1,21):
        if i % j == 0:
            num.append(j)
           
    if (len(num) == 20):
        print(i)
        break
