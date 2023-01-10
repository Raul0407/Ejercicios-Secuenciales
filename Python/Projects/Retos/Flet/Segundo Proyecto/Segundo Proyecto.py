

import flet as ft

vlista = []




def main(page: ft.Page):

    def guardarDatos(e):
        
        vlista.append(textField_Alimentos.value)
        print(vlista)




    page.title="Flet inicio"
    page.scroll = "adaptive"
    texto = ft.Text(value = "Lista de la Compra", color = "blue", size = 25)
    page.add(texto)
    
    textField_Alimentos = ft.TextField(label="Ingredientes",hint_text="Escribe tu lista de la compra (Pulsa el botón + para guardar)")
    page.add(textField_Alimentos)
    
    boton = ft.FloatingActionButton(icon = ft.icons.ADD, on_click = guardarDatos)
    boton2 = ft.FloatingActionButton(icon = ft.icons.ABC)

    row = ft.Row(spacing=100, controls=[boton, boton2])
    page.add(row)

    img = ft.Image(src=f"Imagenes/SuperMercados-Raul.jpeg", width = 300, height = 300)
    page.add(img)

    page.update()
    

ft.app(target = main, assets_dir = "Assets")