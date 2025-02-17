my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


print('a' in my_dict)
print(1 in my_dict)
print(1 in my_dict.values())

print(('a', 2) in my_dict.items())
print(my_list[2])
print(my_dict['d'])

my_list[1:2] = ['20', '25', '33']
print(my_list)
print(my_list[4])