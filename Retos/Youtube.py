#Descargador de videos de Youtube

from pytube import YouTube
from pytube import Playlist

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

'''
Descargar una canción
def descargaCancion(url:str):
    youtube = YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download()

descargaCancion("https://www.youtube.com/watch?v=YVkUvmDQ3HY")
'''

def descargarPlaylist(url:str):
    playlist = Playlist(url)
    for cancion in playlist.videos:
        print("Descargando canción:", cancion.title)
        cancion.streams.get_audio_only().download("Ejercicios-Secuenciales/Canciones/")
        

url = "https://www.youtube.com/playlist?list=PLSFitF4B6yNS82pcRx5XvD1PB6m8lIs5J"
descargarPlaylist("https://www.youtube.com/playlist?list=PLSFitF4B6yNS82pcRx5XvD1PB6m8lIs5J")