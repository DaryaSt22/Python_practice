# Напишите программу, которая возвращает сколько раз слово (именно слово) python встречается в строке
# “Python is a cool language, I want to be more pythonic”
from typing import Counter


def count_words(s: str):
    words = s.split()
    # count.get(i, 0) + 1
    count = Counter(words)

    return count


print(count_words("Python is a cool language, I want to be more pythonic"))
