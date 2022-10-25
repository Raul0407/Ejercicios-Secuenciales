#EJERCICIO 5

letra = (str)(input("Dime una letra (pulsa espacio para salir):\n"))
numero = 0
while letra != " ":
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("Tu letra es una vocal")
    else:
        print("Tu letra no es una vocal")
    letra = (str)(input("Dime una letra (pulsa espacio para salir):\n"))
print("El programa finalizó")