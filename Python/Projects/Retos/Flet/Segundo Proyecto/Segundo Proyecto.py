import flet as ft

def guardarDatos(textField_Alimentos):
    vlista = []
    vlista.append(textField_Alimentos)
    print(vlista)

def main(page: ft.Page):
    page.title="Flet inicio"
    texto = ft.Text(value = "Lista de la Compra", color = "blue", size = 25)
    page.add(texto)
    
    textField_Alimentos = ft.TextField(label="Ingredientes",hint_text="Escribe tu lista de la compra (Pulsa el botón para guardar)")
    page.add(textField_Alimentos)

    boton = ft.FloatingActionButton(icon = ft.icons.ADD, on_click = guardarDatos)
    page.add(boton)
    page.update()

ft.app(target = main)