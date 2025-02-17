pch = [2]
print('введите последнее число')
b = int(input())
for x in range(3, b+1):
    a = 0
    for n in pch:
        if x % n == 0:
            break
        else:
            a = a+1
    if a == len(pch):
        pch.append(x)
pch.insert(0, 1)        
print(pch)
