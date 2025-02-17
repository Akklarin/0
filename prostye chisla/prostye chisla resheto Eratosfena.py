n = int(input("n="))
a = list(range(n+1))
l = [1]
i = 2
while i <= n:
    if a[i] != 0:
        l.append(i) 
        for e in range(i, n+1, i):
            a[e] = 0
    i += 1
print(l)
