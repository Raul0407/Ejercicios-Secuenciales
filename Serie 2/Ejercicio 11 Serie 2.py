#EJERCICIO 11

ladoA = (int)(input("Dime la medida del lado A:\n"))
ladoB = (int)(input("Dime la medida del lado B:\n"))
ladoC = (int)(input("Dime la medida del lado C:\n"))

if (ladoA**2+ladoB**2==ladoC**2) or (ladoA**2+ladoC**2==ladoB**2) or (ladoB**2+ladoC**2==ladoC**2):
    print("Es un triángulo rectángulo")
if (ladoA==ladoB and ladoA!=ladoC) or (ladoA==ladoC and ladoA!=ladoB) or (ladoC==ladoB and ladoA!=ladoA):
    print("Es un triángulo isósceles")   
else:
    if (ladoA==ladoB==ladoC):
        print("Es un triángulo equilátero")
    else:
        print("Es un triángulo escaleno")                