#EJERCICIO 2 
def trianguloArea(base:int, lado:int):
    return base*lado
def trianguloPerímetro(base:int, lado:int):
    return base+base+lado+lado

print("Vamos a calcular el perímetro y el área de un rectángulo\n")
base = (int)(input("Dime la base del triángulo:\n"))
lado = (int)(input("Dime el lado del triángulo:\n"))
print ("El área del rectángulo es:", trianguloArea(base, lado))
print ("El perímetro del rectángulo es:", trianguloPerímetro(base, lado))