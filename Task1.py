# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
#
# строковое представление. Функцию hex используйте для проверки своего результата.

num = int(input("Enter Number: "))

f = format(num, '#x')
print(f)

print()

print(hex(num))