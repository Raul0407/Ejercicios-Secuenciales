#EJERCICIO 10

import math

x1 = (int)(input("Dime la coordenada x de la primera circunferencia:\n"))
y1 = (int)(input("Dime la coordenada y de la primera circunferencia:\n"))
r1 = (int)(input("Dime lel radio de la primera circunferencia:\n"))
x2 = (int)(input("Dime la coordenada x de la segunda circunferencia:\n"))
y2 = (int)(input("Dime la coordenada y de la segunda circunferencia:\n"))
r2 = (int)(input("Dime el radio de la segunda circunferencia:\n"))

distanciacircunferencias = math.sqrt(x2-x1)+(y2-y1)

if distanciacircunferencias > (r1 + r2):
    print("Las circunferencias son exteriores")
if distanciacircunferencias == (r1 + r2):
    print("Las circunferencias son tangentes exteriores")
if distanciacircunferencias < (r1 + r2):
    print("Las circunferencias son secantes")
if distanciacircunferencias == abs(r1-r2):
    print("Las circunferencias son tangentes interiores")
if distanciacircunferencias < abs(r1-r2):
    print("Las circunferencias son interiores")
if distanciacircunferencias == 0:
    print("Las circunferencias son concéntricas")  