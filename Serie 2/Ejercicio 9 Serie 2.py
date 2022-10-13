#EJERCICIO 9

numero1 = (int)(input("Dime un número:\n"))
numero2 = (int)(input("Dime otro número:\n"))
numero3 = (int)(input("Dime otro número:\n"))
if numero1>numero2 and numero1>numero3:
    if numero2>numero3:
        print("El orden sería:", numero1, "mayor que", numero2, "mayor que", numero3)
    else:
        print("El orden sería:", numero1, "mayor que", numero3, "mayor que", numero2)
if numero2>numero1 and numero2>numero3:
    if numero1>numero3:
        print("El orden sería:", numero2, "mayor que", numero1, "mayor que", numero3)
    else:
        print("El orden sería:", numero2, "mayor que", numero3, "mayor que", numero1)        
if numero3>numero1 and numero3>numero2:
    if numero1>numero2:
        print("El orden sería:", numero3, "mayor que", numero1, "mayor que", numero2)
    else:
        print("El orden sería:", numero3, "mayor que", numero2, "mayor que", numero1)        