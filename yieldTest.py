x = int(input())


def n(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


for j in n(x):
    print(j)
