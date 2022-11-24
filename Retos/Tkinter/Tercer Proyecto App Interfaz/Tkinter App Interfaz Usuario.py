from tkinter import *
from tkinter import ttk

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
entry_pass_usuario = ttk.Entry(ventana)

label_repite_pass_usuario = ttk.Label(ventana, text = "Confirma contraseña:")
label_repite_pass_usuario.config(background = "deep sky blue")
entry_repite_pass_usuario = ttk.Entry(ventana)

boton_guardar = ttk.Button(ventana, text = "Guardar")
boton_salir = ttk.Button(ventana, text = "Salir")

#PINTAR EN PANTALLA LOS COMPONENTES
label_titulo.grid(row = 0, column = 0)
label_nombre_usuario.grid(row = 1, column = 0)
entry_nombre_usuario.grid(row = 1, column = 1)

label_pass_usuario.grid(row = 2, column = 0)
entry_pass_usuario.grid(row = 2, column = 1)

label_repite_pass_usuario.grid(row = 3, column = 0)
entry_repite_pass_usuario.grid(row = 3, column = 1)

boton_guardar.grid(row = 4, column = 0)
boton_salir.grid(row = 4, column = 1)

ventana.mainloop()