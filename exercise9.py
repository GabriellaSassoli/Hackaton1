def pythag(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    return False

for a in range(1,1000):

    for b in range(a, 1000 - a ):
        for c in range(b, 1000 - b):
            if (a+b+c == 1000):
                if pythag(a, b, c):
                    print(a,b,c)
                    print("product" .format(a*b*c))
                    break
