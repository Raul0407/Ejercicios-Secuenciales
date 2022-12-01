#EJERCICIO 19

print("El examen es de 20 preguntas")
correctas = (int)(input("Dime cuantas respuestas correctas has tenido:\n"))
incorrectas = (int)(input("Dime cuantas respuestas incorrectas has tenido:\n"))
blanco = (int)(input("Dime cuantas respuestas en blanco has tenido:\n"))
if correctas+incorrectas+blanco==20:
    resultado = (correctas*5)+(incorrectas*-1)+(blanco*0)
    print("Has sacado un total de:", resultado, "puntos sobre 100")
else:
    print("Tus respuestas no suman las 20 preguntas")