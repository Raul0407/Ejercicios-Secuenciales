#EJERCICIO 5

letra = ""
numero = 0
while letra != " ":
    letra = (str)(input("Dime una letra (pulsa espacio para salir):\n")).upper()
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print("Tu letra es una vocal")
    else:
        print("Tu letra no es una vocal")
    letra = (str)(input("Dime una letra (pulsa espacio para salir):\n"))
print("El programa finalizó")

#El programa solo funcionaba cuando pones una minúscula