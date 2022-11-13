#EJERCICIO 18

#Para este ejercicio, preferí verme un video en youtube
#Ya que hacer un bucle infinito con while no tiene sentidoç
#https://www.youtube.com/watch?v=Bt6NnUi70Vo&t=108s
import os
import time
for hora in range(24):
    for minutos in range(60):
        for segundos in range(60):
            os.system('cls')
            print(f'{hora}:{minutos}:{segundos}')
            time.sleep(1)