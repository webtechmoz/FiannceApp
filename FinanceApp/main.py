import flet as ft
from page.Header import Header
from page.Balance import Balance
from page.Moviments import Moviments

def main(page: ft.Page):
    page.bgcolor = ft.colors.with_opacity(0.90, 'white')

    #Definindo as variaveis
    width: int = page.width
    height: int = page.height

    appbar = ft.AppBar(
        toolbar_height=0
    )

    main = ft.SafeArea(
        content=ft.Stack(
            controls=[
                Header(page, width, height),
                Balance(page, width, height),
                Moviments(page, width, height)
            ],
            height=height,
            alignment=ft.alignment.center
        )
    )

    page.add(appbar, main)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.FLET_APP)