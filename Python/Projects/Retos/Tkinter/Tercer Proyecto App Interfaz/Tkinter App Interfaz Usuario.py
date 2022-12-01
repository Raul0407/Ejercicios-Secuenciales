from tkinter import *
from tkinter import ttk
from tkinter import messagebox

usario = ""
contraseña = ""
confirmarcontraseña = ""
genero = ""
vlista = []

def guardarDatos():
    usuario = entry_nombre_usuario.get()
    contraseña = entry_pass_usuario.get()
    confirmarcontraseña = entry_repite_pass_usuario.get()
    genero = combo.get()
    if contraseña == confirmarcontraseña:
        vlista.append(usuario)
        vlista.append(contraseña)
        vlista.append(genero)
    print(vlista)
    entry_nombre_usuario.delete(0, len(usuario))
    entry_pass_usuario.delete(0, len(contraseña))
    entry_repite_pass_usuario.delete(0, len(confirmarcontraseña))
    messagebox.showinfo("Usuario Guardado", f"Usuario {vlista} Guardado Correctamente")

def salirDatos():
    boton_salir = ttk.Button(command = ventana.destroy)


#GENERO LA VENTANA
ventana = Tk()
ventana.title("Registrarse o Iniciar Sesión")
ventana.geometry("250x300")
ventana.resizable()
ventana.config(background="deep sky blue")

#TÏTULO
label_titulo = ttk.Label(ventana, text = "---INTRODUCE AQUÍ TUS DATOS---")
label_titulo.config(background = "deep sky blue")

#TEXTO NOMBRE, USUARIO Y BOTÖN GUARDAR
label_nombre_usuario = ttk.Label(ventana, text = "Nombre Usuario:")
label_nombre_usuario.config(background = "deep sky blue")
entry_nombre_usuario = ttk.Entry(ventana)

label_pass_usuario = ttk.Label(ventana, text = "Contraseña:")
label_pass_usuario.config(background = "deep sky blue")
entry_pass_usuario = ttk.Entry(ventana, show = "*")

label_repite_pass_usuario = ttk.Label(ventana, text = "Confirma contraseña:")
label_repite_pass_usuario.config(background = "deep sky blue")
entry_repite_pass_usuario = ttk.Entry(ventana, show = "*")

combolabel = ttk.Label(ventana, text = "Dime tu género")
combolabel.config(background = "deep sky blue")

boton_guardar = ttk.Button(ventana, text = "Guardar", command = guardarDatos)
boton_salir = ttk.Button(ventana, text = "Salir", command = ventana.destroy)

#PINTAR EN PANTALLA LOS COMPONENTES
label_titulo.grid(row = 0, column = 0, pady = 10, padx = 15)
label_nombre_usuario.grid(row = 1, column = 0, pady = 10)
entry_nombre_usuario.grid(row = 1, column = 1, pady = 10)

label_pass_usuario.grid(row = 2, column = 0, pady = 10)
entry_pass_usuario.grid(row = 2, column = 1, pady = 10)

label_repite_pass_usuario.grid(row = 3, column = 0, pady = 10)
entry_repite_pass_usuario.grid(row = 3, column = 1, pady = 10)

boton_guardar.grid(row = 5, column = 0, pady = 10)
boton_salir.grid(row = 5, column = 1, pady = 10)

combolabel.grid(row = 4, column = 0, pady = 10)
combo = ttk.Combobox(ventana, values = ["Masculino", "Femenino"])
combo.grid(row = 4, column = 1, pady = 10) 



ventana.mainloop()