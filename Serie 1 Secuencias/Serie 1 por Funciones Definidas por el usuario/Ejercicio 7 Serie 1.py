#EJERCICIO 7
def horas(minutos:int):
    return int(minutos/60)
def minutos(minutos:int):
    return minutos%60

minutos = (int)(input("Dime una cantidad de minutos:\n"))
print("Son", horas(minutos), "horas y", minutos(minutos), "minutos")