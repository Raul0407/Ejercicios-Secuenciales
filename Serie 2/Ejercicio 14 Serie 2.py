#EJERCICIO 14

precioinicial = (int)(input("Dime el precio inicial de la uva:\n"))
uva = (str)(input("Dime el tipo de uva (A o B):\n"))
tamaño = (int)(input("Dime el tamaño (1 o 2):\n"))

if uva == "A":
    if tamaño == 1:
        print("Tu uva vale:", precioinicial+0.2, "euros")
    elif tamaño == 2:
        print("Tu uva vale:", precioinicial+0.3, "euros")
    else:
        print("Ese tamaño de uva no existe")
else:
    if uva == "B":
        if tamaño == 1:
            print("Tu uva vale:", precioinicial-0.3, "euros")
        elif tamaño == 2:
            print("Tu uva vale:", precioinicial-0.5, "euros")
        else:
            print("Ese tamaño de uva no existe")       
    else:
        print("Ese tipo de uva no existe")