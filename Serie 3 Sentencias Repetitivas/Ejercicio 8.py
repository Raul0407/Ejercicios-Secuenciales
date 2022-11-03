#EJERCICIO 8

numeros = 1
sumaintervalos = 0
fueraintervalos = 0
igualesintervalos = 0
limiteinferior = (int)(input("Dime el límite inferior:\n"))
limitesuperior = (int)(input("Dime el límite superior:\n"))
while limiteinferior>limitesuperior:
    print("ERROR---El límite inferior es mayor al superior")
    limiteinferior = (int)(input("Dime el límite inferior:\n"))
    limitesuperior = (int)(input("Dime el límite superior:\n"))

while numeros != 0:
    numeros = (int)(input("Dime números (pulsa 0 para salir):\n"))
    if numeros == 0:
        print("Programa Finalizado --- Datos:")
    if numeros > limiteinferior and numeros < limitesuperior:
        sumaintervalos = sumaintervalos + numeros
    if numeros < limiteinferior and numeros !=0 or numeros > limitesuperior and numeros != 0:
        fueraintervalos += 1
    if numeros == limiteinferior or numeros == limitesuperior:
        igualesintervalos += 1
print("La sume de intervalos dentro del límite es:", sumaintervalos)
print("Hay:", fueraintervalos, "números fuera del límite")
print("Hay:", igualesintervalos, "números iguales a los límites")