# Напишите функцию char_count(s: str), которая возвращает словарь
# количества вхождений каждого символа в переданной строке

from collections import Counter

def char_count(s: str):
    return dict(Counter(s))

print(char_count("abc"))
print(char_count("ab"))