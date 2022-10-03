#EJERCICIO 8

salario = (int)(input("Primero, dime tu salario:\n"))
venta1 = (int)(input("Ahora, dime el precio de tu primera venta:\n"))
venta2 = (int)(input("Ahora, dime el precio de tu segunda venta:\n"))
venta3 = (int)(input("Ahora, dime el precio de tu tercera venta:\n"))
ventatotal = ((venta1*0.10)+(venta2*0.10)+(venta3*0.10))
print("Ganarías solo con las ventas, un toal de:", ventatotal)
print("Ganarías un total de:", ventatotal+salario)