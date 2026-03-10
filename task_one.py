# Напишите функцию prod_or_sum(n1: int, n2: int) возвращающую произведение двух чисел,
# если оно меньше 1000, иначе их сумму


def prod_or_sum(n1: int, n2: int):
    mult = n1 * n2

    if mult < 1000:
        return mult
    else:
        return n1 + n2

print(prod_or_sum(500, 500))
