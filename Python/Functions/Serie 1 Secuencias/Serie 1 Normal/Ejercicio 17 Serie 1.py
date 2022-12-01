#EJERCICIO 17

horasinicio = (int)(input("¿A qué hora has salido?:\n"))
minutosinicio = (int)(input("¿En qué minuto has salido?:\n"))
segundosinicio = (int)(input("¿En qué segundo has salido?:\n"))
tiempodeltrayecto = (int)(input("¿Cuánto tiempo has tardado (en segundos)?\n"))
tiempototalinicio = horasinicio*3600+minutosinicio*60+segundosinicio
tiempofinal = tiempototalinicio + tiempodeltrayecto
horadellegada = tiempofinal//3600
minutodellegada = tiempofinal%3600//60
segundodellegada = tiempofinal%3600%60
print("Llegaste a las:", horadellegada, "Horas", minutodellegada, "Minutos y", segundodellegada, "Segundos")