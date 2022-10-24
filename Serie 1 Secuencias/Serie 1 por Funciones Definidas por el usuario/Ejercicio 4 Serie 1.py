#EJERCICIO 4

def suma(numero1:int, numero2:int):
    return numero1+numero2
def resta(numero1:int, numero2:int):
    return numero1-numero2
def multiplicacion(numero1:int, numero2:int):
    return numero1*numero2
def division(numero1:int, numero2:int):
    return numero1/numero2

numero1 = (int)(input("Dime un número:\n"))
numero2 = (int)(input("Dime otro número:\n"))
print("La suma de esos números es:", suma(numero1, numero2))
print("La resta de esos números es:", resta(numero1, numero2))
print("La multiplicación de esos números es:", multiplicacion(numero1, numero2))
print("La división de esos números es:", division(numero1, numero2))