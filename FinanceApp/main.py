import flet as ft
from page.Header import Header, user
from page.Balance import Balance
from page.Moviments import Moviments
from page.Extract import Extract
from page.Actions import Actions
from page.Favorities import Favorities
from page.BottomBar import BottomBar
import asyncio

async def main(page: ft.Page):
    page.bgcolor = ft.colors.with_opacity(0.90, 'white')

    #Definindo as variaveis
    width: int = page.width - 20
    height: int = page.height

    appbar = ft.AppBar(
        toolbar_height=0
    )

    main = ft.SafeArea(
        content=ft.Stack(
            controls=[
                ft.Stack(
                    controls=[
                        await Header(page, width, height),
                        Balance(page, width, height, user['user']),
                        ft.Column(
                            controls=[
                                Moviments(page, width, height, user['user']),
                                Actions(page, width, height, user['user']),
                                Favorities(page, width, height, user['user']),
                                Extract(page, width, height, user['user'])
                            ],
                            width=width,
                            height=height * 0.66,
                            top=height*0.21,
                            scroll=ft.ScrollMode.HIDDEN,
                        ),
                        BottomBar(page, width, height, user['user'])
                    ],
                    visible=True
                )
            ],
            height=height,
            alignment=ft.alignment.center
        )
    )

    page.add(appbar, main)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.FLET_APP)