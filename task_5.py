# Напишите функцию, same_ends(l: List) возвращающую значение True, если первое
# и последнее число в переданном списке совпадают. Если числа разные, верните False.
from typing import List


def same_ends(l: List):
    if l[0] == l[-1]:
        return True
    else:
        return False

print(same_ends([1, 2, 3, 4, 5, 1]))