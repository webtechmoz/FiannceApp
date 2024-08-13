import flet as ft

def Moviments(page: ft.Page, width: int, height: int, moviments: list[float] = [2520.81, 1350.56]) -> ft.ResponsiveRow:

    control = ft.ResponsiveRow(
        controls=[
            ft.Container(
                bgcolor=ft.colors.WHITE,
                col={'xs': 10, 'sm': 10},
                height= height * 0.15,
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
                                            value=f'MT {format(moviments[0], ",.2f")}',
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
                                            value=f'MT {format(moviments[1], ",.2f")}',
                                            size=20,
                                            color=ft.colors.with_opacity(0.9, 'red'),
                                            weight='bold'
                                        )
                                    ],
                                    spacing=1
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
        top=height * 0.20,
        alignment=ft.MainAxisAlignment.CENTER
    )

    return control