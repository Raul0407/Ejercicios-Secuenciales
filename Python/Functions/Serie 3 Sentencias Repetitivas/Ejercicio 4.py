#EJERCICO 4

listanumero = []
contadorMenor0 = 0
contadorMayor0 = 0
contadorIgual0 = 0 
cantidad = (int)("Dime la cantidad de números que vas a introducir:\n")

for i in range(1,cantidad):
    numero = (int)(input("Dime un número:\n"))
    listanumero.append(numero)

for i in listanumero:
    if i==0:
        contadorIgual0+=1
    elif i<0:
        contadorMenor0+=1
    elif i>0:
        contadorMayor0+=1

print("Hay:", contadorMayor0, "numeros mayores que 0, ", contadorIgual0, "iguales que 0 y", contadorMenor0, "menores de 0")