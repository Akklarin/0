print("Сколько первых членов последовательности вы хотите увидеть?")

num = int(input())

print("Пожалуйста:")


def f(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return f(num-1)+f(num-2)


for num in range(1, num+1):
    print(str(num)+":"+str(f(num)))
