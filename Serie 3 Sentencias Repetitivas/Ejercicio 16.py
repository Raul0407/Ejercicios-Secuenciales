#EJERCICIO 16

horastrabajadas = 0
trabajadores = (int)(input("Dime la cantidad de empleados:\n"))
sueldo = (int)(input("Dime cuanto cobran a la hora:\n"))
for i in range(1, trabajadores + 1):
    horassemanales = (int)(input("Dime las horas que ha trabajo:\n"))
    horastrabajadas += horassemanales
    print("Este trabajador cobrará en total:", horastrabajadas*sueldo)
print("Programa finalizado")