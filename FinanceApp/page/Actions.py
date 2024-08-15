import flet as ft
from utils.details import buttons

def Actions(page: ft.Page, width: int, height: int, user: str) -> ft.ResponsiveRow:

    control = ft.ResponsiveRow(
        controls=[
            ft.Container(
                col={'xs': 12, 'sm': 12},
                height=height*0.10,
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                padding=ft.padding.all(8),
                alignment=ft.alignment.center,
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Container(
                                    width=50,
                                    height=50,
                                    border_radius=50,
                                    bgcolor=ft.colors.with_opacity(0.08, 'black'),
                                    content=ft.Icon(
                                        name=buttons[button]['icon'],
                                        size=30,
                                        color=ft.colors.BLUE
                                    )
                                ),
                                ft.Text(
                                    value=buttons[button]['title'],
                                    size=12,
                                    weight='bold',
                                    color=ft.colors.with_opacity(0.30, 'black'),
                                    text_align=ft.TextAlign.CENTER
                                )
                            ],
                            spacing=0,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ) for button in buttons
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                )
            )
        ]
    )

    return control