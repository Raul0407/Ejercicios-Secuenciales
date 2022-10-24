#EJERCICIO 3

import math

def hipotenusa(cateto1:int, cateto2:int):
    return math.sqrt(cateto1*cateto1+cateto2*cateto2)


cateto1 = (int)(input("Dime el cateto número 1:\n"))
cateto2 = (int)(input("Dime el cateto número 2:\n"))
print("La hipotenusa es:", hipotenusa(cateto1, cateto2))