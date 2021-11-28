print("Привет!")
x = float(0)
y = float(0)
print("Ваша позиция по умолчанию ({0};{1})".format(x,y))
x = float(input("Введите значения координаты X:"))
y = float(input("Введите значения координаты Y:"))
print("Ваша позиция сейчас ({0};{1})".format(x,y))

#_____________________________________________________________
print("Привет!")
g = bool(True)
print("Ваша позиция по умолчанию (0;0)")

x = float(input("Введите значения координаты X:"))
y = float(input("Введите значения координаты Y:"))
print("Теперь Вы в точке ({0};{1})".format(x,y))
print("Далее указывайте шаг X и Y, чтобы менять положение!")
while ( g == True):
    
    step = float(input("Введите шаг по X: "))
    x += step
    step = float(input("Введите шаг по Y: "))
    y += step
    print("Ваша позиция сейчас ({0};{1})".format(x,y))

    f = (input("Хотите закончить (yes/no)? "))
    if f == 'yes' or f =='y':
        break
    else:
        continue


