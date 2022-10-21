#EJERCICIO 5

def celsius(farenheit:int):
    return (farenheit-32)*(5/9)

farenheit = (int)(input("Dime los grados Farenheit:\n"))
print("Son:", celsius(farenheit), "grados Celsius")