#EJERCICIO 19

opcion = 0
def pintaMenu(opcion:int):
    vNombres = []
    vTelefonos = []
    opcion = 0
    while opcion < 5 or opcion>5:
        print("-----Menú Agenda-----")
        print("1-Insertar Contácto")
        print("2-Borrar Contácto")
        print("3-Buscar Contácto")
        print("4-Ver todos los Contáctos")
        print("5-Salir")
        try:
            opcion = (int)(input("Introduce una opción:\n"))
        except:
            print("Las opciones son de la 1 a la 5")
    return opcion
    
    print("Saliste de la base de datos")

pintaMenu("Has seleccionado", pintaMenu(opcion))