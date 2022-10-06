#EJERCICIO 20

doseuros = (int)(input("Dime cuantas monedas tienes de 2 euros:\n"))
uneuro = (int)(input("Dime cuantas monedas tienes de 1 euro:\n"))
cincuentacentimos = (int)(input("Dime cuantas monedas tienes de 50 centimos:\n"))
veintecentimos = (int)(input("Dime cuantas monedas tienes de 20 centimos:\n"))
diezcentimos = (int)(input("Dime cuantas monedas tienes de 10 centimos:\n"))
monedaseuros = doseuros+uneuro
centimos = cincuentacentimos*0.5+veintecentimos*0.2+diezcentimos*0.10
dinerototal = monedaseuros+centimos
print("En total, tienes:", dinerototal, "euros")