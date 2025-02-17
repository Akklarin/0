pch = [2]
print('введите последнее число')
b = int(input())
for x in range(3, b):
    a = 0
    for n in pch:
        if x % n == 0:
            break
        else:
            a = a+1
    # print('a = '+str(a))
    # print('длина списка = '+str(len(pch)))
    if a == len(pch):
        print(str(x) + ' подходит')
        pch.append(x)
    else:
        print(str(x)+' не подходит')

        
print(pch)
