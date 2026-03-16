# Написать функцию, in_fib(n: int), возвращающую True если,
# число есть в последовательности чисел фибоначчи, иначе False

def in_fib(n: int):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n


print(in_fib(10))
print(in_fib(100))
print(in_fib(1))