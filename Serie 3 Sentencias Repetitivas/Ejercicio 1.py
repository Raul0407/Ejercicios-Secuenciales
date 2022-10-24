#EJERCICIO 1

contador = 0
multiplicacion = 1
numero = (int)(input("Dime un número:\n"))
for contador in range(1, numero+1):
    multiplicacion = multiplicacion * contador
print("Su factorial es:", multiplicacion)