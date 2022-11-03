#EJERCICIO 9

base = (int)(input("Dime la base de la potencia:\n"))
exponente = (int)(input("Dime el exponente de la potencia:\n"))
potencia = 1
while exponente <= 0:
    exponente = (int)(input("El exponente no puede ser negativo, inténtalo de nuevo:\n")) 
for i in range(1, exponente+1):
    potencia = potencia * base
print("EL resultado de la potencia es:", potencia)