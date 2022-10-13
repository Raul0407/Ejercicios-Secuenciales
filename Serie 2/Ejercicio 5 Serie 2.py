#EJERCICIO 5

usuario = (str)(input("Dime tu usuario:\n"))
usuariooriginal = "Pepe"
contrasena = (str)(input("Dime tu contraseña:\n"))
contrasenaoriginal = "asdasd"
if usuario==usuariooriginal:
    if contrasena==contrasenaoriginal:
        print("Entrando al sistema...")
    else:
        print("La contraseña no es correcta")
else:
    print("El usuario no es correcto")