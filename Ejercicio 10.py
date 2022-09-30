#EJERCICIO 10

parcial1 = (int)(input("Dime la nota del parcial 1:\n"))
parcial2 = (int)(input("Dime la nota del parcial 2:\n"))
parcial3 = (int)(input("Dime la nota del parcial 3:\n"))
examen = (int)(input("Dime la nota del examen final:\n"))
trabajo = (int)(input("Dime la nota del trabajo:\n"))
print("Tendrás una nota de:", (((parcial1+parcial2+parcial3)/3)*0.55)+(examen*0.30)+(trabajo*0.15))