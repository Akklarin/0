def decorator(func):
    def wrap():
        print('================')
        func()
        print('================')
    return wrap

@decorator
def print_text():
    print('Hello world!')


print_text()
