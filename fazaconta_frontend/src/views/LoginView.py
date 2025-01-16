import re
import flet as ft
from fazaconta_frontend.src.api.ApiClient import api_client
from fazaconta_frontend.src.components.Button import Button
from fazaconta_frontend.src.components.Input import Input
from fazaconta_frontend.src.constants import (
    BORDER_RADIUS,
    DEEPBLUE,
    LIGHTBLUE,
    MEDIUMBLUE,
    PINK,
    VIEW_HEIGHT,
    VIEW_WIDTH,
    Routes,
)
from fazaconta_frontend.src.utils import is_authenticated


class LoginView(ft.View):
    page: ft.Page
    is_private: bool
    email_input: Input
    password_input: Input

    def __init__(self, page: ft.Page, is_private: bool = False):
        super().__init__(
            route=Routes.LOGIN.value,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        self.page = page
        self.is_private = is_private

        self.email_input = Input(
            label="E-mail",
            hint_text="Insira aqui o e-mail: ",
            border_color=MEDIUMBLUE,
            text_style=ft.TextStyle(color=LIGHTBLUE),
            focused_border_color=PINK,
            validation_fn=self.validate_email,
        )

        self.password_input = Input(
            label="Senha",
            hint_text="Insira aqui a senha: ",
            border_color=MEDIUMBLUE,
            text_style=ft.TextStyle(color=LIGHTBLUE),
            focused_border_color=PINK,
            validation_fn=self.validate_password,
            password=True,
            can_reveal_password=True,
        )

        self.login_button = Button("Entrar", on_click=self.on_submit)

        self.controls = [self._main_content(page)]

    def did_mount(self):
        super().did_mount()
        if is_authenticated(self.page):
            self.page.go(Routes.GROUPS_LIST)

    def validate_email(self, email):
        if not email:
            return "O e-mail é obrigatório."
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, email):
            return "Insira um e-mail válido."
        return None

    def validate_password(self, password):
        if not password:
            return "A senha é obrigatória."
        return None

    def show_snackbar(self, message, color=ft.colors.RED):
        snackbar = ft.SnackBar(ft.Text(message), bgcolor=color)
        self.page.snack_bar = snackbar
        self.page.snack_bar.open = True
        self.page.update()

    def on_login_sucess(self, data):
        self.show_snackbar("Login realizado com sucesso!", color=ft.colors.GREEN)
        self.page.client_storage.set("token", data)
        self.page.go(Routes.GROUPS_LIST.value)

    def on_login_error(self, message: str, exc: Exception):
        print(f"Erro no login: {message}")
        self.show_snackbar(message, color=ft.colors.RED)

    def on_submit(self, e):
        email_valid = self.email_input.validate()
        password_valid = self.password_input.validate()

        if not (email_valid and password_valid):
            return

        email = self.email_input.value
        password = self.password_input.value

        self.login_button.set_loading_state(True)

        api_client.login(
            email=email,
            password=password,
            on_success=self.on_login_sucess,
            on_error=self.on_login_error,
        )

        self.login_button.set_loading_state(False)

    def _main_content(self, page: ft.Page):
        return ft.Container(
            alignment=ft.alignment.center,
            width=VIEW_WIDTH,
            height=VIEW_HEIGHT,
            bgcolor=DEEPBLUE,
            border_radius=BORDER_RADIUS,
            content=ft.Column(
                width=400,
                controls=[
                    ft.Row(
                        [
                            ft.Container(
                                ft.Icon(
                                    ft.icons.ARROW_BACK_IOS_NEW_ROUNDED, color=LIGHTBLUE
                                ),
                                margin=ft.margin.only(left=15, right=10, top=20),
                                on_click=lambda _: page.go(Routes.HOME.value),
                            ),
                            ft.Container(
                                width=100,
                                margin=ft.margin.only(left=215, right=10, top=20),
                                content=ft.TextButton(
                                    "Criar conta",
                                    style=ft.ButtonStyle(
                                        color=LIGHTBLUE, bgcolor=DEEPBLUE
                                    ),
                                    on_click=lambda _: page.go(Routes.REGISTER.value),
                                ),
                            ),
                        ]
                    ),
                    ft.Container(
                        width=400,
                        margin=ft.margin.only(left=150, right=10, top=30),
                        content=ft.Text(
                            "Login",
                            size=30,
                            color=LIGHTBLUE,
                            weight=ft.FontWeight.W_700,
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
                        content=self.email_input,
                    ),
                    ft.Container(
                        width=400,
                        margin=ft.margin.only(left=20, right=20, top=15),
                        content=self.password_input,
                    ),
                    ft.Container(
                        width=200,
                        margin=ft.margin.only(left=90, right=20, top=15),
                        content=ft.TextButton("Esqueceu a senha?"),
                    ),
                    ft.Container(
                        width=100,
                        margin=ft.margin.only(left=140, right=20, top=10),
                        content=self.login_button,
                        alignment=ft.alignment.center,
                    ),
                ],
            ),
        )
