import flet as ft
from utils.details import moviments

def Moviments(page: ft.Page, width: int, height: int, user: str) -> ft.ResponsiveRow:

    control = ft.ResponsiveRow(
        controls=[
            ft.Container(
                bgcolor=ft.colors.WHITE,
                col={'xs': 12, 'sm': 12},
                height= height * 0.14,
                border_radius=8,
                padding=ft.padding.only(
                    top=10,
                    left=8,
                    right=8
                ),
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='Úlitmos 28 dias',
                            color=ft.colors.with_opacity(0.4, 'black'),
                            size=14,
                            weight='bold'
                        ),
                        ft.Divider(
                            height=1,
                            thickness=2,
                            color=ft.colors.with_opacity(0.12, 'black'),
                        ),
                        ft.Row(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            value='Entradas',
                                            size=16,
                                            color=ft.colors.with_opacity(0.6, 'black'),
                                            weight='bold'
                                        ),
                                        ft.Text(
                                            value=f'MT {format(moviments[user]['0'], ",.2f")}',
                                            size=20,
                                            color=ft.colors.with_opacity(0.9, 'green'),
                                            weight='bold'
                                        )
                                    ],
                                    spacing=1
                                ),

                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            value='Saídas',
                                            size=16,
                                            color=ft.colors.with_opacity(0.6, 'black'),
                                            weight='bold'
                                        ),
                                        ft.Text(
                                            value=f'MT {format(moviments[user]['1'], ",.2f")}',
                                            size=20,
                                            color=ft.colors.with_opacity(0.9, 'red'),
                                            weight='bold'
                                        )
                                    ],
                                    spacing=3
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ],
                    spacing=6
                )
            )
        ],
        width=width,
        alignment=ft.MainAxisAlignment.CENTER
    )

    return control