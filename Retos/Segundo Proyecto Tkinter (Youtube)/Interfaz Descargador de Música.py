from tkinter import *
from tkinter import ttk
from pytube import YouTube
from pytube import Playlist

#FUNCION PYTUBE
def descargaCancion(url:str):
    url = datos_Entrada.get()
    youtube = YouTube(url)
    print(youtube.author)
    cancion = youtube.streams.get_audio_only()
    cancion.download()


#GENERO LA VENTANA
ventana = Tk()
ventana.title("Descargador de vídeos de Youtube")
ventana.geometry("250x300")
ventana.resizable()
ventana.config(background="deep sky blue")

datos_Entrada = ttk.Entry(ventana)
datos_Entrada.place(x=850, y=100) 

boton_Descargar = ttk.Button(ventana, text = "Descargar", command=descargaCancion)
boton_Descargar.place(x=890, y=125)

label_titulo = ttk.Label(ventana, text = "Introduce la URL del vídeo")
label_titulo.config(background = "gold")
label_titulo.place(x=845, y=75)

ventana.mainloop()