#AGENDA DE TELËFONOS

'''
Opción 1:
Lista para nombres
Lista para teléfonos

Opción 2:
Lista para nombres y teléfonos
Ejemplo: [Juan - Teléfono, Pepe - Teléfono]
'''

#Opción 1

vNombres = []
vTelefonos = []

nombre = (str)(input("Dime un nombre:\n"))
telefono = (int)(input("Dime su telefono:\n"))

vNombres.append(nombre)
vTelefonos.append(telefono)

print(vNombres)
print(vTelefonos)

print("El nombre de tu contacto es:", vNombres, "su número es:", vTelefonos)