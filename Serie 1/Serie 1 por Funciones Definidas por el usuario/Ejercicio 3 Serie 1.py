#EJERCICIO 3

import math

def Hipotenusa(cateto1:int, cateto2:int):
    print("Vamos a calculart la hipotenusa de un triángulo rectángulo\n")
    hipotenusa = math.sqrt(cateto1*cateto1+cateto2*cateto2)


cateto1 = (int)(input("Dime el cateto número 1:\n"))
cateto2 = (int)(input("Dime el cateto número 2:\n"))
print("La hipotenusa es:", Hipotenusa)