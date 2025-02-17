import timeit # замер времени


def fib(n):
    return 1 if n == 0 or n == 1 else fib(n - 1) + fib(n - 2)


print(fib(30))
# вывод времени работы
print(timeit.timeit('fib(30)', number=100, globals=globals()))


# import timeit
# 
#
# def fib(n, cache=None):
#     if n == 0 or n == 1: return 1
#
#     if cache is None: cache = {}
#     if n in cache: return cache[n]
#
#     result = fib(n - 1, cache) + fib(n - 2, cache)
#     cache[n] = result
#
#     return result
#
#
# print(fib(30))
# print(timeit.timeit('fib(30)', number=100, globals=globals()))