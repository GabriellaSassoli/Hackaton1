
sum = 0
primes = []
for i in range(2,20000):

    for j in range(2, i):
        if not i % j:
            break
    else:
        primes.append(i)
        sum = sum + i
print(sum)