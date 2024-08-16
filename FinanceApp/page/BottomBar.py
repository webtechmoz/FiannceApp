import flet as ft

def BottomBar(page: ft.Page, width: int, height: int, user: str) -> ft.ResponsiveRow:

    control = ft.ResponsiveRow(
        controls=[
            ft.Container(
                bgcolor=ft.colors.WHITE,
                border_radius=8,
                height=height*0.06,
                padding=ft.padding.only(
                    left=8,
                    right=8
                ),
                content=ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.HOME,
                            icon_size=40,
                            icon_color=ft.colors.BLUE
                        ),
                        ft.IconButton(
                            icon=ft.icons.SETTINGS,
                            icon_size=40,
                            icon_color=ft.colors.BLUE
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )
        ],
        width=width,
        top=height * (1 - 0.12)
    )

    return control