#EJERCICIO 11

numero = (int)(input("Dime un número y te diré si es primo:\n"))
contador = 0
for i in range(2, numero):
    if numero % i == 0:
        contador +=1
if contador >= 1:
    print("Tu número no es primo")
else:
    print("Tu número es primo")