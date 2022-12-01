from tkinter import *
from tkinter import ttk

#GENERO LA VENTANA
ventana = Tk()
ventana.title("Primer Ejercicio")
ventana.geometry("250x300")
ventana.resizable()
ventana.config(background="gold")
ventana.i

#GENERO EL LIENZO PARA PINTAR COMPONENTES
frm = ttk.Frame(ventana).pack() #o .pack

#COMPONENTES LABEL Y BUTTOM
labelTexto = ttk.Label(frm, text="Hola Tkinter") #o .pack
labelTexto.config(background="light blue", border=5, font=("Arial", 15))
labelTexto.pack()

ttk.Button(ventana, text="Salir", command=ventana.destroy).pack() #o .pack
ventana.mainloop()