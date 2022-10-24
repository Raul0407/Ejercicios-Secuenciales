#EJERCICIO 8

nota = (int)(input("Dime tu nota:\n"))
edad = (int)(input("Dime tu edad:\n"))
sexo = (str)(input("Dime tu sexo (M o F):\n"))
if sexo=="M" and edad>=18 and nota>=5:
    print("Posible")
elif(sexo=="F" and edad>=18 and nota>=5):
    print("Posiblee")
else:
    print("No aceptada")