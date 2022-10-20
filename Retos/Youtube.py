#Descargador de videos de Youtube

from pytube import YouTube

''' Opción de Juanfran
print("Empezando")
link = "https://www.youtube.com/watch?v=YVkUvmDQ3HY"
yt = YouTube(link)

for pistas in yt.streams:
    print(pistas)

mp3 = yt.streams.get_audio_only()
print("Descargando")
mp3.download()
'''


def descargaCancion(url:str):
    youtube = YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download()

descargaCancion("https://www.youtube.com/watch?v=YVkUvmDQ3HY")