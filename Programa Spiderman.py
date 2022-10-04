#PROGRAMA SPIDERMAN

distancia1 = (int)(input("Dime la distancia 1:\n"))
distancia2 = (int)(input("Dime la distancia 2:\n"))
if abs(distancia1)>abs(distancia2):
    print("Primero deberás de ir al destino 2")
    distanciat = abs(distancia1)+abs(distancia2)*2
    print("La distancia recorrida sería:", (distanciat))
else:
    print("Primero deberás de ir al destino 1")
    distanciat = abs(distancia1)*2+abs(distancia2)
    print("La distancia recorrida sería:", (distanciat))