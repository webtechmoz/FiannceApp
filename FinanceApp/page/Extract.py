import flet as ft
from utils.details import extract

def Extract(page: ft.Page, width: int, height: int, user: str) -> ft.ResponsiveRow:

    control = ft.ResponsiveRow(
        controls=[
            ft.Container(
                col={'xs': 12, 'sm': 12},
                height=height*0.25,
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                padding=ft.padding.only(
                    top=10,
                    left=8,
                    right=8,
                    bottom=8
                ),
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='Últimos movimentos',
                            color=ft.colors.with_opacity(0.4, 'black'),
                            size=14,
                            weight='bold'
                        ),
                        ft.Divider(
                            height=1,
                            thickness=2,
                            color=ft.colors.with_opacity(0.08, 'black')
                        ),
                        ft.Column(
                            controls=[
                                ft.ResponsiveRow(
                                    controls=[
                                        ft.Text(
                                            value=extract[user][str(i)]['data'],
                                            col={'xs': 3},
                                            color=ft.colors.with_opacity(0.5, 'black')
                                        ),
                                        ft.Text(
                                            value=extract[user][str(i)]['descrição'] if len(extract[user][str(i)]['descrição']) <= 15 else f"{extract[user][str(i)]['descrição'][:16]}...",
                                            col={'xs': 5},
                                            color=ft.colors.with_opacity(0.5, 'black')
                                        ),
                                        ft.Text(
                                            value=f"MT {format(extract[user][str(i)]['montante'], ',.2f')}",
                                            col={'xs': 4},
                                            weight='bold',
                                            text_align=ft.TextAlign.END,
                                            color=ft.colors.with_opacity(0.8, 'green') if extract[user][str(i)]['tipo'] == '0' else ft.colors.with_opacity(0.8, 'red')
                                        )
                                    ],

                                ) for i in range(1, len(extract[user])+1)
                            ]
                        )
                    ]
                )
            )
        ]
    )

    return control