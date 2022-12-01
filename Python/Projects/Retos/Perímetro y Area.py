#EJERCICIO CLASE

def rectanguloArea(base:int, lado:int):
    return base*lado
def rectanguloPerímetro(base:int, lado:int):
    return base+base+lado+lado
def lista():
    vLista = []
    vLista.append(rectanguloPerímetro)
    vLista.append(rectanguloArea)
    return vLista

print("Vamos a calcular el perímetro y el área de un rectángulo\n")
base = (int)(input("Dime la base del triángulo:\n"))
lado = (int)(input("Dime el lado del triángulo:\n"))
print ("El área del rectángulo es:", rectanguloArea(base, lado))
print ("El perímetro del rectángulo es:", rectanguloPerímetro(base, lado))
print ("El perímetro y el area son: ", lista(base, lado))