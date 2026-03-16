# Написать функцию, fib_list(n: int), возвращающую список первых n чисел фибоначчи

def fib_list(n: int):
    a, b = 0, 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fib_list(10))