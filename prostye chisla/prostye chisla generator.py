def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n == 0:
            return False
    return True


def prime_generator(b):
    for number in range(2, b):
        if is_prime(number):
            yield number 
    
    
t = int(input())

ln = (list(prime_generator(t)))
ln.insert(0, 1)
print(ln)
