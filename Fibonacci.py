#n=[x for x in range(1,1000)]
sum = 0

def F(n):
    if n == 1: return 1
    elif n == 2: return 2
    else:return F(n-1)+F(n-2)

#for i in n:
 #   print(F(i))
i = 1
while F(i) < 1000000:
        if F(i) % 2 == 0 :
            sum = sum + F(i)
            print("i get in the module ", F(i))
        i+= 1
print (sum)