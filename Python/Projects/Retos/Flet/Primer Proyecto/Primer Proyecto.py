import flet as ft

def main(page: ft.Page):
    page.title="Flet inicio"
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
    
    textField_Nombre = ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    page.add(textField_Nombre)
    dropDown_Menu = ft.Dropdown(width=300,options=[ft.dropdown.Option("Hombre")])
    page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Mujer"))
    page.update()

    slider_edad=ft.Slider(min=0,max=120,divisions=120,label="Edad{value}")
    page.add(slider_edad)
    #Crear fila
    fila = ft.Row(controls=[textField_Nombre,dropDown_Menu])
    page.add(fila)

ft.app(target = main)