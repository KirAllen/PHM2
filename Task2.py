# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
#
# Для проверки своего кода используйте модуль fractions.
import fractions

a = input("Введите первую дробь: ")
b = input("ведите вторую дробь: ")
num1 = 0
num2 = 0
num3 = 0
num4 = 0

for i in range(len(a)):
        num1 = int(a[:a.index("/")])
        num2 = int(a[a.index("/")+1:])

for i in range(len(b)):
    num3 = int(b[:b.index("/")])
    num4 = int(b[b.index("/")+1:])



print(num1/num2 + num3/num4)

print((num1/num2) * (num3/num4))

print("______________________________________________")
firstfraction = fractions.Fraction(num1, num2)
secondfraction = fractions.Fraction(num3, num4)

print(firstfraction+secondfraction)
print(firstfraction*secondfraction)