#EJERCICIO 16

v1 = (int)(input("Dime la velocidad del vehículo 1 (en km/h):\n"))
v1enmetros = v1*1000/3600
v2 = (int)(input("Dime la velocidad del vehículo 2 (en km/h):\n"))
v2enmetros = v2*1000/3600
if v1enmetros<v2enmetros:
    print("Nunca se encontrarán, porque el coche 1 va más lento")
else:
    if v1enmetros == v2enmetros:
        print("Nunca se encontrarán, porque los 2 coches van a la misma velocidad")
    else:
        distancia = (int)(input("Dime la distancia entre ellos (en km):\n"))
        posicioncoche1 = 0
        distanciaenmetros = distancia*1000
        posicioncoche2 = distanciaenmetros

            #Fórmula = posicionfinalcoche1=posicioninicialcoche1*v1(t)
            #Fórmula2 = posicionfinalcoche1=posicioninicialcoche2*v2(t)

        tiempo = posicioncoche2/(v1enmetros+v2enmetros)
        print("Tardarían en encontrarse:", tiempo, "minutos")