primes = []

for i in range (1,1000000):
    for j in range(2, i):
        if not i % j:
            break
    else:
        primes.append(i)
print(primes)
print("the 10 001th number is", primse[10001])