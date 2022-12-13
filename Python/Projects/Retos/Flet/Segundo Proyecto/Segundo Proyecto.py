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


    
    boton = ft.FloatingActionButton(icon = ft.icons.ADD, on_click = guardarDatos, )
    page.add(boton)
    boton2 = ft.FloatingActionButton(icon = ft.icons.ABC)
    page.add(boton2)
    page.update()
    

ft.app(target = main)