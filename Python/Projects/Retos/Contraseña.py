#CONTRASEÑA

contrasena = "Raul"
palabra = "y"
intentos = 0
while (palabra != contrasena) and (intentos<4):
    palabra = (str)(input("Dime la contraseña:\n"))
    intentos = intentos + 1
if (intentos==4):
    print("Intentos agotados, inténtelo de nuevo más tarde")
else:
    print("Entraste")