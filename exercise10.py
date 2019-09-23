
sum = 0
primes = []
for i in range(2,2000000):
    print(primes)
    for j in range(2, i):
        if not i % j:
            break
    else:
        primes.append(i)
        sum = sum + i
print(sum
      )