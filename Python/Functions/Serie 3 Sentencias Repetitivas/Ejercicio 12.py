#EJERCICIO 12

ahorromes = []
ahorrototal = 0
for i in range(1, 13):
    ahorro = (int)(input("¿Cuánto has ahorrado este mes?\n"))
    ahorromes.append(ahorro)
    ahorrototal = ahorro + ahorrototal
print("Has ahorrado en total:", ahorrototal)
mes = int(input("Dime un mes en número (del 0 al 11):\n"))
print("En ese mes ahorraste", ahorromes[mes])
acumulado = 0
for x in range(mes+1):
    acumulado += ahorromes[x]
print("En ese mes ahorraste acumulado", acumulado)