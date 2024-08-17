import flet as ft
from utils.details import users
import asyncio
import httpx

user = users['1']

async def Header(page: ft.Page, width: int, height: int) -> ft.ResponsiveRow:

    async def logar(e: ft.ControlEvent):
        stack: ft.Stack = e.control.parent.parent.parent.parent.parent.parent

        stack.controls.append(
            ft.ResponsiveRow(
                width=width,
                height=height,
                controls=[
                    ft.Container(
                        bgcolor=ft.colors.WHITE,
                        col={'xs': 12, 'sm': 12},
                        border_radius=10,
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(
                            top=100,
                            left=8,
                            right=8
                        ),

                        content=ft.Column(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Icon(
                                            name=ft.icons.KEY,
                                            size=30,
                                            color='blue'
                                        ),
                                        ft.Text(
                                            value='Login'.upper(),
                                            size=18,
                                            weight='bold',
                                            color=ft.colors.BLACK
                                        ),
                                    ],
                                    spacing=0,
                                    width=width,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                ),
                                ft.ResponsiveRow(
                                    controls=[
                                        ft.TextField(
                                            hint_text='Username',
                                            hint_style=ft.TextStyle(
                                                color=ft.colors.with_opacity(0.4, 'black'),
                                                size=15,
                                                weight='bold'
                                            ),
                                            text_style=ft.TextStyle(
                                                color=ft.colors.with_opacity(0.8, 'black'),
                                                size=15,
                                                weight='bold'
                                            ),
                                            prefix_icon=ft.icons.PERSON,
                                            border=ft.InputBorder.OUTLINE,
                                            border_width=1,
                                            border_color=ft.colors.with_opacity(0.4, 'black')
                                        ),
                                        ft.TextField(
                                            hint_text='Password',
                                            hint_style=ft.TextStyle(
                                                color=ft.colors.with_opacity(0.4, 'black'),
                                                size=15,
                                                weight='bold'
                                            ),
                                            text_style=ft.TextStyle(
                                                color=ft.colors.with_opacity(0.8, 'black'),
                                                size=15,
                                                weight='bold'
                                            ),
                                            prefix_icon=ft.icons.KEY,
                                            border=ft.InputBorder.OUTLINE,
                                            border_width=1,
                                            border_color=ft.colors.with_opacity(0.4, 'black')
                                        ),
                                        ft.FloatingActionButton(
                                            text='Login',
                                            foreground_color='white',
                                            bgcolor='blue',
                                            height=50
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.TextButton(
                                                    text='Forgot password',
                                                    style=ft.ButtonStyle(
                                                        color='blue',
                                                        bgcolor=ft.colors.TRANSPARENT
                                                    ),
                                                    height=50
                                                ),
                                                ft.TextButton(
                                                    text='Create account',
                                                    style=ft.ButtonStyle(
                                                        color='blue',
                                                        bgcolor=ft.colors.TRANSPARENT
                                                    ),
                                                    height=50
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                        )
                                    ]
                                )
                            ],
                            spacing=20
                        )
                    )
                ]
            )
        )

        page.update()

    control = ft.ResponsiveRow(
        controls=[
            ft.Container(
                col={'xs': 12, 'sm': 12},
                height=height * 0.20,
                border_radius=4,
                bgcolor=ft.colors.with_opacity(0.8, 'blue'),
                padding=ft.padding.only(
                    top=12,
                    left=10,
                    right=10
                ),
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(
                                    value='Bem vindo,',
                                    size=15,
                                    weight='bold',
                                    color='white'
                                ),
                                ft.Text(
                                    value=user['name'],
                                    size=22,
                                    weight='bold',
                                    color='white'
                                )
                            ],
                            spacing=0
                        ),
                        ft.Column(
                            controls=[
                                ft.Container(
                                    width=45,
                                    height=45,
                                    border_radius=45,
                                    bgcolor=ft.colors.with_opacity(0.8, 'grey'),
                                    content=ft.Icon(
                                        name=ft.icons.PERSON,
                                        size=30
                                    ),
                                    on_click=lambda e: asyncio.run(logar(e))
                                )
                            ]
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        width=width,
        top=0,
        left=0
    )

    lambda e: asyncio.run(logar(e))

    return control