#TABLA DE MULTIPLICAR

numero = (int)(input("Dime un número y te diré su tabla de multiplicar:\n"))
multiplicacion = 0
while (multiplicacion<=10):
    print(numero, "x", multiplicacion, "=", numero*multiplicacion)
    multiplicacion = multiplicacion + 1