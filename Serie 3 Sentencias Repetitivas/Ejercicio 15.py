#EJERCICIO 15

pagototal = 0
primerpago = 10
for mes in range(1, 21):
	pagototal = pagototal + primerpago
	primerpago = primerpago * 2
print("En total, tras los 20 meses paga un total de: ",pagototal, "euros")