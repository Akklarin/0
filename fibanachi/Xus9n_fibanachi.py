num = int(input())
for num in range(1, num):
    a = 1
    b = 1
    for x in range(1, num):
        a = a + b
        b = a - b
    print(a)
