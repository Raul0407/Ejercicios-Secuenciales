#EJERCICIO 17

trabajadores = (int)(input("Dime la cantidad de empleados:\n"))
sueldoporhora = (int)(input("Dime cuanto cobran a la hora:\n"))
horastotales = 0
for i in range(1, trabajadores + 1):
    diastrabajados = (int)(input("Dime la cantidad de días que ha trabajado:\n"))
    for a in range(1, diastrabajados + 1):
        print("Día:", a)
        horastrabajadas = (int)(input("Dime las horas que ha trabajado este día:\n"))
        horastotales += horastrabajadas
    print("Este trabajador cobrará:", horastotales*sueldoporhora)