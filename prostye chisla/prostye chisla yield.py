pch=[2]
print('введите последнее число')
b = int(input())

def nn(x, list):
        a=0
        for n in list:
            if x%n == 0:
                break
            else:
                a=a+1
        if a==len(list):
                yield x

for i in range(3,b+1):
      for i in nn(i, pch): 
         pch.append(i)


pch.insert(0, 1)        
print(pch)