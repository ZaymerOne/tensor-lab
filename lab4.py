
from random import randint
 
N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print("Список до сортировки: ", a)
 
for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("Список после сортировки: ", a)

#__________________________________________
dict = {'red':(255, 0, 0), 'green':(0,128,0), 'blue':(0,0,255)}
print(dict)

#__________________________________________
a1 = {50, 15, 10}
a2 = {50, 18, 0}
print(a1)
print(a2)
print(a1.intersection(a2))
print(a1.difference(a2))
print(a2.difference(a1))
print(a1.symmetric_difference(a2))
