#EJERCICIO 7

base = (int)(input("Dime la base:\n"))
exponente = (int)(input("Dime el exponente:\n"))
if exponente==0:
    print("El esponente es 0, or lo que siempre saldrá 1")
else:
    if exponente>0:
        print("Su potencia es:", pow(base, exponente))
    else:
        print("Su potencia es:", pow(1/base, exponente))