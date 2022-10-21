#EJERCICIO 9

def compraTotal(compra:int):
    return compra*0.85

compra = (int)(input("Cuanto vale tu compra:\n"))
print("Tendrás que pagar:", compraTotal(compra), "Euros gracias al 15% de descuento")