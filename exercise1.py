

numbers=[x for x in range(1,1001)];
num = 0;
sum = 0;


for num in numbers:

    if num % 3 == 0 or num % 5 == 0:

        sum = sum + num

print(sum);


