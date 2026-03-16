# Написать функцию, fib_list(n: int), возвращающую список первых n чисел фибоначчи
import time

def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time()-t))
        return res

    return tmp

@timer
def fib_list(n: int):
    a, b = 0, 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fib_list(10))