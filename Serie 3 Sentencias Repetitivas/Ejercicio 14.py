#EJERCICIO 14

#Opción 1
km1 = 150
km2 = 70
distanciaee = km1 - km2
velocidadcoches = (int)(input("Dime la velocidad de los coches (en m/s):\n"))
tiempo = distanciaee/(velocidadcoches*2)
distcanciacoche1 = velocidadcoches * tiempo
encuentro = 150 - distcanciacoche1
print("Tardarán un total de:", tiempo, "horas y se encuentran en el kilometro:", encuentro)

#Opción
while km1 != km2:
    km1 = km1-1
    km2 = km2 +1
print("Se encuentran en el km:", km1)