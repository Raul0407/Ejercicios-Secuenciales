#EJERCICIO 2 

def rectanguloArea(base:int, lado:int):
    return base*lado
def rectanguloPerímetro(base:int, lado:int):
    return base+base+lado+lado

print("Vamos a calcular el perímetro y el área de un rectángulo\n")
base = (int)(input("Dime la base del triángulo:\n"))
lado = (int)(input("Dime el lado del triángulo:\n"))
print ("El área del rectángulo es:", rectanguloArea(base, lado))
print ("El perímetro del rectángulo es:", rectanguloPerímetro(base, lado))