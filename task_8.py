# Напишите функцию is_palindrome(n: int), проверяющую,
# является ли данное число числом-палиндромом

def is_palindrome(n: int):
    n = str(n)
    return n == n[::-1]

print(is_palindrome(123))
print(is_palindrome(1231))
print(is_palindrome(1221))