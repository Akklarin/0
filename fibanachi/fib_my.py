n = int(input('n = '))
a = 1
b = 1
e = 1
while e < (n+1)//2:
    a = a + b
    b = a + b
    e += 1
if n % 2 == 1:
    print(a)
else:
    print(b)
