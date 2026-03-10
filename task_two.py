# Задание 2
#
#
#
# Напишите программу, которая перебирает первые 10 чисел и на каждой итерации выводит сумму текущего и предыдущего числа. (поможет range())
#
#
# Пример вывода:
# Current Number: 0, Previous Number 0, Sum: 0
# …
# Current Number: 3, Previous Number 2, Sum: 5
# Current Number: 4, Previous Number 3, Sum: 7
# …
#
# Current Number: 9, Previous Number 8, Sum: 17

for i in range(11):
    print(i)
    print(f"Current Number: {i}, Previous Number: {i-1}, Sum: {i + (i-1)}")


