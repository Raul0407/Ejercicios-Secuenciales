#EJERCICIO 13

porcenta = 0
horas = 0
horastotal = 0
for i in range(1, 7):
    horas = (int)(input("¿Cuántas horas ha trabajado este día?\n"))
    horastotal = horas + horastotal
for a in range(1,horastotal+1):
    porcenta += 1
sueldo = (int)(input("Dime tu sueldo:\n"))
total = sueldo*(porcenta/100) + sueldo
print("Recibirás un:", porcenta, "% más en base a tu sueldo, que sería:", total, "euros")