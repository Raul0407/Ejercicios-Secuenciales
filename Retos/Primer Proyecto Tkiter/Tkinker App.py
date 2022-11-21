from tkinter import *
from tkinter import ttk
import tkinter as tk

def Saludar():
    texto = campoTexto.get()
    textoLabel.set(texto)

#GENERO LA VENTANA
ventana = Tk()
ventana.title("Primer Ejercicio")
ventana.geometry("250x300")
ventana.resizable()
ventana.config(background="deep sky blue")
icono = tk.PhotoImage(file="images.png")
ventana.iconbitmap(icono)

#GENERO EL LIENZO PARA PINTAR COMPONENTES
frm = ttk.Frame(ventana).pack() #o .pack

#COMPONENTES LABEL Y BUTTOM
textoLabel = StringVar()
textoLabel.set("Hola Tkinter")
labelTexto = ttk.Label(frm, textvariable=textoLabel) #o .pack
labelTexto.config(background="gold", border=5, font=("Arial", 15))
labelTexto.pack()

#COMPONENTE CUADRO DE TEXTO
campoTexto = ttk.Entry(frm)
campoTexto.pack()

ttk.Button(ventana, text="Te digo lo que escribes", command = Saludar).pack() #o .pack
ttk.Button(ventana, text="Salir", command=ventana.destroy).pack() #o .pack

ventana.mainloop()