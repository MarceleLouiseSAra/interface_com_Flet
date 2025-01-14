import flet as ft
import requests

DEEPBLUE = "#432350"
MEDIUMBLUE = "#b476ff"
PINK = "#f4c9fd"
WHITE = "#ffffff"
LIGHTBLUE = "#B0C4DE"

page: ft.Page


def view_log_in_page(page: ft.Page) -> ft.Container:

    username_input = ft.TextField(
        label="Usuário",
        hint_text="Insira aqui o nome de usuário: ",
        border_color=MEDIUMBLUE,
        text_style=ft.TextStyle(color=LIGHTBLUE),
        autofocus=True,
        focused_border_color=PINK,
    )

    password_input = ft.TextField(
        label="Senha",
        hint_text="Insira aqui a senha: ",
        border_color=MEDIUMBLUE,
        text_style=ft.TextStyle(color=LIGHTBLUE),
        autofocus=True,
        password=True,
        can_reveal_password=True,
        focused_border_color=PINK,
    )

    def on_submit(e):  # análogo ao request_data
        username = username_input.value
        password = password_input.value
        # VALIDAÇÕES AQUI
        print(f"Usuário:", {username}, "Senha:", {password})
        page.go("/home_page")

    def request_data(e):
        user_name = username_input.value
        password = password_input.value

        body = {"user_name": user_name, "password": password}

        r = requests.get("http://localhost:8000/users", data=body)
        print(r.json())
        page.go("/home_page")

    log_in_page = ft.Container(
        width=400,
        height=850,
        bgcolor=DEEPBLUE,
        border_radius=20,
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        content=ft.Column(
            # alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=400,
            controls=[
                ft.Row(
                    [
                        ft.Container(
                            ft.Icon(
                                ft.icons.ARROW_BACK_IOS_NEW_ROUNDED, color=LIGHTBLUE
                            ),
                            margin=ft.margin.only(left=15, right=10, top=20),
                            on_click=lambda _: page.go("/"),
                        ),
                        ft.Container(
                            width=100,
                            margin=ft.margin.only(left=215, right=10, top=20),
                            content=ft.TextButton(
                                "Criar conta",
                                style=ft.ButtonStyle(color=LIGHTBLUE, bgcolor=DEEPBLUE),
                                on_click=lambda _: page.go("/sign_in_page"),
                            ),
                        ),
                    ]
                ),
                ft.Container(
                    width=400,
                    margin=ft.margin.only(left=150, right=10, top=30),
                    content=ft.Text(
                        "Log in", size=30, color=LIGHTBLUE, weight=ft.FontWeight.W_700
                    ),
                ),
                ft.Container(
                    width=400,
                    margin=ft.margin.only(left=10, right=10, top=30),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        "Por favor, preencha as informações a seguir:",
                        size=16,
                        color=LIGHTBLUE,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ),
                ft.Container(
                    width=400,
                    margin=ft.margin.only(left=20, right=20, top=30),
                    content=ft.Column(controls=[username_input]),
                ),
                ft.Container(
                    width=400,
                    margin=ft.margin.only(left=20, right=20, top=15),
                    content=ft.Column(controls=[password_input]),
                ),
                ft.Container(
                    width=200,
                    margin=ft.margin.only(left=90, right=20, top=15),
                    content=ft.TextButton("Esqueceu a senha?"),
                ),
                ft.Container(
                    width=100,
                    margin=ft.margin.only(left=140, right=20, top=10),
                    content=ft.TextButton(
                        "Entrar",
                        style=ft.ButtonStyle(
                            color={
                                ft.ControlState.HOVERED: LIGHTBLUE,
                                ft.ControlState.FOCUSED: WHITE,
                                ft.ControlState.DEFAULT: PINK,
                            },
                            bgcolor=MEDIUMBLUE,
                        ),
                        on_click=lambda e: on_submit(e),  # trocar pela request_data
                    ),
                ),
            ],
        ),
    )

    return log_in_page
