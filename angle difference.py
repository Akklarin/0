def diff(a, b):
    e = (max(a, b) - min(a, b))//360
    return min(abs(max(a, b) - 360*e - min(a, b)), abs(max(a, b) - 360*(e+1) - min(a, b)))


d = diff(int(input()), int(input()))
print(d)
