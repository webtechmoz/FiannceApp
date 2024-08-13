import flet as ft

def Balance(page: ft.Page, width: int, height: int, balance: float = 1280.90) -> ft.ResponsiveRow:

    control = ft.ResponsiveRow(
        controls=[
            ft.Container(
                col={'xs': 6, 'sm': 6},
                height=height * 0.1,
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='Saldo Disponível',
                            size=14,
                            color='white',
                            weight='bold'
                        ),
                        ft.Text(
                            value=f'MT {format(balance, ",.2f")}',
                            size=25,
                            color='white',
                            weight='bold'
                        ),
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        top=height* 0.085,
        width=width,
        alignment=ft.MainAxisAlignment.CENTER
    )

    return control