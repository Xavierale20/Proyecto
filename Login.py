import flet as ft

conteiner = ft.Container(
    ft.Column([
        ft.Container(
            ft.Text(
                'Inicio de Sesión',
                width=320,
                size=30,
                text_align='center',
                weight='w900'
            ),
            padding=ft.padding.only(20, 20)
        ),
        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text='Nombre de Usuario',
                border='underline',
                color='black',
                prefix_icon=ft.icons.VERIFIED_USER_ROUNDED
            ),
            padding=ft.padding.only(20, 20)
        ),
        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text='Contraseña',
                border='underline',
                color='black',
                prefix_icon=ft.icons.LOCK,
                password=True
            ),
            padding=ft.padding.only(20, 20)
        ),
        ft.Container(
            ft.ElevatedButton(
                text='Iniciar',
                width=280,
                bgcolor='black'
            ),
            padding=ft.padding.only(20, 20)
        ),
        ft.Container(
            ft.Row([
                ft.Text('¿Desea crear un usuario?'),
                ft.TextButton('Crear Usuario')
            ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )



    ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    ),




    border_radius=20,
    width=320,
    height=500,
    gradient=ft.LinearGradient([
        ft.colors.BROWN


    ])


)


def main(page: ft.Page):
    page.bgcolor = 'black'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.add(conteiner)


ft.app(target=main)
