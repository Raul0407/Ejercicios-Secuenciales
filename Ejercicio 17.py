#EJERCICIO 17

horasinicio = (int)(input("¿A qué hora has salido?:\n"))
minutosinicio = (int)(input("¿En qué minuto has salido?:\n"))
segundosinicio = (int)(input("¿En qué segundo has salido?:\n"))
tiempodeltrayecto = (int)(input("¿Cuánto tiempo has tardado (en segundos)?"))
tiempototalinicio = horasinicio*3600+minutosinicio*60+segundosinicio
tiempofinal = tiempototalinicio + tiempodeltrayecto