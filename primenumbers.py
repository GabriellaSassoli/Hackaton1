import math
check_me = range(100000, int( math.sqrt(600851475143)))

primes = [3]
for i in check_me:
    print(primes)
    for j in range(2, i):
        if not i % j:
            break
    else:
        primes.append(i)
print(primes)

sum = []
for i in primes:
    if 600851475143 % i == 0:
        sum.append(i)

print (sum)