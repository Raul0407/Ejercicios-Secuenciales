#EJERCICIO 2

import random

numerosecreto = random.randint(1, 100)
intentos = 1
numerointentado = (int)(input("Dime un número:\n"))

while numerointentado != numerosecreto and intentos<10:
    if numerointentado<numerosecreto:
        print("El número secreto es mayor")
    else:
        print("El número secreto es menor")
    intentos += 1
    print("Llevas:", intentos, "intentos")
    numerointentado = (int)(input("Dime otro número:\n"))

if numerointentado == numerosecreto:
    print("Lo has adivinado en:", intentos, "intentos")
else:
    print("Has perdido")