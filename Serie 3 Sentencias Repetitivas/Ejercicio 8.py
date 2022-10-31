#EJERCICIO 8

lista = []
numeros = 1
sumaintervalos = 0
limiteinferior = (int)(input("Dime el límite inferior:\n"))
limitesuperior = (int)(input("Dime el límite superior:\n"))
while limiteinferior>limitesuperior:
    print("ERROR---El límite inferior es mayor al superior")
    limiteinferior = (int)(input("Dime el límite inferior:\n"))
    limitesuperior = (int)(input("Dime el límite superior:\n"))

while numeros != 0:
    numeros = (int)(input("Dime números (pulsa 0 para salir):\n"))
    lista.append(numeros)

if lista > limiteinferior and lista < limitesuperior
print("La suma de los números dentro de los intervalos es:", sumaintervalos)