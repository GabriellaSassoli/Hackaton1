import math


sum = 0
sumsquart = 0
for i in range(1,101):
    sum = sum + i
    sumsquart = sumsquart + i*i

sum = sum*sum

print(sum - sumsquart)