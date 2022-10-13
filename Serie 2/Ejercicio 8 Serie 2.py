#EJERCICIO 8

nota = (int)(input("Dime tu nota:\n"))
edad = (int)(input("Dime tu edad:\n"))
sexo = (str)(input("Dime tu sexo (M o F):\n"))
if sexo=="M":
    if nota>=5:
        if edad>18:
            print("Posible")
        else:
            print("No aceptada")
    print("No aceptada")
else:
    if sexo=="F":
        if nota>=5:
            if edad>18:
                print("Aceptada")
            else:
                print("No aceptada")
        print("No aceptada")
    else:
        print("Tu sexo no es correcto")

#Revisar en clase