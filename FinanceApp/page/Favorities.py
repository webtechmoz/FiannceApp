import flet as ft

def Favorities(page: ft.Page, width: int, height: int, user: str) -> ft.ResponsiveRow:

    control = ft.ResponsiveRow(
        controls=[
            ft.Container(
                bgcolor=ft.colors.WHITE,
                border_radius=8,
                col={'xs': 12, 'sm': 12},
                height=height*0.20,
                padding=ft.padding.only(
                    top=10,
                    left=8,
                    right=8
                ),
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='Favoritos',
                            color=ft.colors.with_opacity(0.4, 'black'),
                            size=14,
                            weight='bold'
                        ),
                        ft.Divider(
                            height=1,
                            thickness=2,
                            color=ft.colors.with_opacity(0.12, 'black'),
                        ),
                    ]
                )
            )
        ]
    )

    return control