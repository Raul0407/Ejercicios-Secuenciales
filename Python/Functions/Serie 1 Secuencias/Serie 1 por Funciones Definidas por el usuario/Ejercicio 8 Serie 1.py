#EJERCICIO 8

def ventaTotal(salario:int, venta1:int, venta2:int, venta3:int):
    return ((venta1*0.10)+(venta2*0.10)+(venta3*0.10))
def resultado(salario:int, venta1:int, venta2:int, venta3:int):
    return (venta1*0.10)+(venta2*0.10)+(venta3*0.10)+salario

salario = (int)(input("Primero, dime tu salario:\n"))
venta1 = (int)(input("Ahora, dime el precio de tu primera venta:\n"))
venta2 = (int)(input("Ahora, dime el precio de tu segunda venta:\n"))
venta3 = (int)(input("Ahora, dime el precio de tu tercera venta:\n"))
print("Ganarías solo con las ventas, un total de:", ventaTotal(salario, venta1, venta2, venta3))
print("Ganarías un total de:", resultado(salario, venta1, venta2, venta3))