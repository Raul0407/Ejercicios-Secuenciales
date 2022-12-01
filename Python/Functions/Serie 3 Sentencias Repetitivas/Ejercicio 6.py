#EJERCICIO 6

numero1 = (int)(input("Dime un número:\n"))
numero2 = (int)(input("Dime otro número:\n"))
pares = 0
for i in range(numero1, numero2+1):
    if i % 2 == 0:
        pares = pares + 1
    else:
        pares = pares + 0
print("Hay ", pares, "numeros pares")