#EJERCICIO 12

año = (int)(input("Dime el año y te diré si es bisiesto:\n"))
if (año % 4 == 0 and not año % 100 == 0 or año % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")