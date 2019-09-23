
x = range(100,999)
y = range(100,999)
#print(x)
polindrom = []

for i in x:
    for j in y:
        num = i *j
        if (str(num) == str(num)[::-1]):
            polindrom.append(num)

print(polindrom[-1])