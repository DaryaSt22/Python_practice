# Задание 4
# Напишите функцию cut_str(s: str, n: int) удаляющую первые n символов из переданной
# строки (как мы помним строки неизменяемы, так что придется вернуть новую строку)

def cut_str(s: str, n: int):
    result = s[n:]
    return result

print(cut_str("hello", 3))
print(cut_str("hello", 4))