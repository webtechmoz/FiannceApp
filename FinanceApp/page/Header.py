import flet as ft

def Header(page: ft.Page, width: int, height: int, name: str = 'Web Tech') -> ft.ResponsiveRow:

    control = ft.ResponsiveRow(
        controls=[
            ft.Container(
                col={'xs': 12, 'sm': 12},
                height=height * 0.25,
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
                                    value=name,
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
                                    )
                                )
                            ]
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ]
    )

    return control