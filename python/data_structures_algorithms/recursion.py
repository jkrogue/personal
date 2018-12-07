def get_fib(idx):
    if idx < 2:
        return idx
    else:
        return get_fib(idx - 1) + get_fib(idx - 2)
        
print(get_fib(0))
print(get_fib(1))
print(get_fib(2))
print(get_fib(3))
print(get_fib(4))
print(get_fib(5))
print(get_fib(6))
