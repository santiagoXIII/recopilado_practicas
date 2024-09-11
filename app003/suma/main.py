import flet as ft

def sumar(text_field, text_field2, page):
    primer =int(text_field.value)
    segundo =int(text_field2.value)
    resul=primer+segundo
    dialog= ft.AlertDialog(
        title=ft.Text("resultado"),
        content=ft.Text(f"el resultado es:{resul}"),
        actions=[
            ft.TextButton("Da click para salir", on_click=lambda e: close_dialog(page))]
    )

def limpiar(text_field, text_field2, page):
    text_field = ft.TextField(label="")
    text_field2 = ft.TextField(label="")

    page.dialog =dialog
    page.dialog.open = True
    page.update()

def close_dialog(page):
    page.dialog.open = False
    page.update()

def main(page: ft.Page):
    page.title="caulculadora"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="blue"

    lbl1=ft.Text("primer numero",
                 style=ft.TextStyle(size=40,weight="bold"))

    lbl2=ft.Text("segundo numero",
                 style=ft.TextStyle(size=40,weight="bold"))

    Img1=ft.Image(src="pinguino.jpg",width=200,height=200)

    btnsumar=ft.ElevatedButton("sumar",
                            color="green",
                            width=100,
                            height=50,
                            on_click=lambda e: sumar(text_field,text_field2, page))

    btnlimpiar=ft.ElevatedButton("limpiar",
                            color="red",
                            width=100,
                            height=50,
                            on_click=lambda e: limpiar(text_field,text_field2, page))

    text_field = ft.TextField(label="")

    text_field2 = ft.TextField(label="")

    def limpiar(e):
        page.update()

    page.add(
        ft.Row([Img1,ft.Column([lbl1,text_field,lbl2,text_field2,ft.Row([btnsumar,btnlimpiar])]),],
               alignment=ft.MainAxisAlignment.CENTER,)
    )

ft.app(target=main)
