import math

a = float(input("Введите число a:" ))
b = float(input("Введите число b:"))
c = a + b
print("a + b = ",c)
c = a - b
print("a - b = ",c)
c = a * b
print("a * b = ",c)
c = a / b
print("a / b = ",c)
c = a ** b
print("a ** b = ",c)
c = a % b
print("a % b = ",c)
c = a // b
print("a // b = ",c)

d = input("Введите свое имя: ")
print("Hello, "+ d + " !")

s = list(input("Введите слово: "))
print("Результат среза: ", s[-1:-3:-1])

print("Ищем площадь окружности S")
r = float(input("Введите радиус окружности r: "))
print("S = pi * r**2 = ", math.pi * (r ** 2))
