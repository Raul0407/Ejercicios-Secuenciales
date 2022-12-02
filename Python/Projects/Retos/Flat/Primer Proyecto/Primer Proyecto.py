import flet as ft

def main(page: ft.Page):

    def cambiarColor(e):
        for i in range(11):
            text = ft.Text(value = f"Texto número {i}", size = 12.5)
            page.add(text)
            texto.color = "red"
            page.update()
    
    #COMPONENTE TEXTO
    texto = ft.Text(value = "Introducción a Flet", color = "yellow", size = 25)
    page.add(texto) #ADD SIRVE PARA AÑADIR Y ACTUALIZAR
    texto.value = "Cambiando los datos"

    #COMPONENTE BOTÖN
    boton = ft.FloatingActionButton(icon = ft.icons.ADD, on_click=cambiarColor)
    page.add(boton)

    page.update()

ft.app(target = main)