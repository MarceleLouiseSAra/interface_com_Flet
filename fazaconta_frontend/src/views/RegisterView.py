import re
import flet as ft
from fazaconta_frontend.src.api.ApiClient import api_client
from fazaconta_frontend.src.components.Button import Button
from fazaconta_frontend.src.components.Input import Input
from fazaconta_frontend.src.components.ProfileImagePicker import ProfileImagePicker
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
from fazaconta_frontend.src.dtos.PixType import PixType


class RegisterView(ft.View):
    page: ft.Page
    is_private: bool
    name_input: Input
    email_input: Input
    password_input: Input
    confirm_password_input: Input
    nickname_input: Input
    pix_type_dropdown: ft.Dropdown
    pix_value_input: Input
    phone_number_input: Input
    profile_photo_path: str | None

    def __init__(self, page: ft.Page, is_private: bool = False):
        super().__init__(
            route=Routes.REGISTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        self.page = page
        self.is_private = is_private

        self.profile_photo_path = None
        self.profile_image_picker = ProfileImagePicker(
            page=self.page, on_image_change=self.on_profile_image_selected
        )

        self.name_input = Input(
            label="Nome de usuário",
            hint_text="Insira aqui o nome de usuário",
            border_color=MEDIUMBLUE,
            text_style=ft.TextStyle(color=LIGHTBLUE),
            focused_border_color=PINK,
            validation_fn=self.validate_name,
        )

        self.email_input = Input(
            label="E-mail",
            hint_text="Insira aqui o e-mail",
            border_color=MEDIUMBLUE,
            text_style=ft.TextStyle(color=LIGHTBLUE),
            focused_border_color=PINK,
            validation_fn=self.validate_email,
        )

        self.password_input = Input(
            label="Senha",
            hint_text="Insira aqui a senha",
            border_color=MEDIUMBLUE,
            text_style=ft.TextStyle(color=LIGHTBLUE),
            focused_border_color=PINK,
            validation_fn=self.validate_password,
            password=True,
            can_reveal_password=True,
        )

        self.confirm_password_input = Input(
            label="Confirmar senha",
            hint_text="Insira novamente a senha",
            border_color=MEDIUMBLUE,
            text_style=ft.TextStyle(color=LIGHTBLUE),
            focused_border_color=PINK,
            validation_fn=self.validate_confirm_password,
            password=True,
            can_reveal_password=True,
        )

        self.phone_number_input = Input(  # Phone number input
            label="Número de telefone",
            hint_text="Insira aqui o número de telefone",
            border_color=MEDIUMBLUE,
            text_style=ft.TextStyle(color=LIGHTBLUE),
            focused_border_color=PINK,
            validation_fn=self.validate_phone_number,
        )

        self.nickname_input = Input(
            label="Apelido",
            hint_text="Insira aqui o apelido",
            border_color=MEDIUMBLUE,
            text_style=ft.TextStyle(color=LIGHTBLUE),
            focused_border_color=PINK,
            validation_fn=self.validate_nickname,
        )

        self.pix_type_dropdown = ft.Dropdown(
            options=[
                ft.dropdown.Option(PixType.EMAIL.value, "E-mail"),
                ft.dropdown.Option(PixType.CPF_CNPJ.value, "CPF/CNPJ"),
                ft.dropdown.Option(PixType.PHONE_NUMBER.value, "Telefone"),
                ft.dropdown.Option(PixType.RANDOM.value, "Aleatório"),
            ],
            label="Tipo de chave Pix",
            border_color=MEDIUMBLUE,
            focused_border_color=PINK,
        )

        self.pix_value_input = Input(
            label="Chave Pix",
            hint_text="Insira aqui a chave Pix",
            border_color=MEDIUMBLUE,
            text_style=ft.TextStyle(color=LIGHTBLUE),
            focused_border_color=PINK,
            validation_fn=self.validate_pix_value,
        )

        self.sign_up_button = Button("Criar conta", on_click=self.on_submit)

        self.controls = [self._main_content(page)]

    def on_profile_image_selected(self, image_path):
        self.profile_photo_path = image_path

    def validate_name(self, name):
        if not name:
            return "O nome de usuário é obrigatório."
        if len(name) < 3:
            return "O nome de usuário deve ter pelo menos 3 caracteres."
        return None

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
        if len(password) < 6:
            return "A senha deve ter pelo menos 6 caracteres."
        return None

    def validate_confirm_password(self, confirm_password):
        if confirm_password != self.password_input.value:
            return "As senhas não correspondem."
        return None

    def validate_phone_number(self, phone_number):
        if not phone_number:
            return "O número de telefone é obrigatório."
        pattern = r"^\+55\s?\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"
        if not re.match(pattern, phone_number):
            return "Insira um número de telefone válido no formato +55 (XX) XXXXX-XXXX."
        return None

    def validate_nickname(self, nickname):
        if not nickname:
            return "O apelido é obrigatório."
        return None

    def validate_pix_value(self, pix_value):
        pix_type = self.pix_type_dropdown.value
        if not pix_type:
            return "Selecione o tipo de chave Pix."
        if not pix_value:
            return "Insira uma chave Pix válida."
        return None

    def show_snackbar(self, message, color=ft.colors.RED):
        snackbar = ft.SnackBar(ft.Text(message), bgcolor=color)
        self.page.snack_bar = snackbar
        self.page.snack_bar.open = True
        self.page.update()

    def on_sign_up_success(self, data):
        self.show_snackbar("Conta criada com sucesso!", color=ft.colors.GREEN)
        self.page.go(Routes.LOGIN.value)

    def on_sign_up_error(self, message: str, exc: Exception):
        print(f"Erro na criação da conta: {message}")
        self.show_snackbar(message, color=ft.colors.RED)

    def on_submit(self, e):
        name_valid = self.name_input.validate()
        email_valid = self.email_input.validate()
        password_valid = self.password_input.validate()
        confirm_password_valid = self.confirm_password_input.validate()
        nickname_valid = self.nickname_input.validate()
        pix_valid = self.pix_value_input.validate()

        if not all(
            [
                name_valid,
                email_valid,
                password_valid,
                confirm_password_valid,
                nickname_valid,
                pix_valid,
            ]
        ):
            return

        self.sign_up_button.set_loading_state(True)

        api_client.create_user(
            name=self.name_input.value,
            email=self.email_input.value,
            password=self.password_input.value,
            nickname=self.nickname_input.value,
            pix_type=self.pix_type_dropdown.value,
            pix_value=self.pix_value_input.value,
            phone_number=self.phone_number_input.value,
            image_path=self.profile_photo_path,
            on_success=self.on_sign_up_success,
            on_error=self.on_sign_up_error,
        )

        self.sign_up_button.set_loading_state(False)

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
                                on_click=lambda _: page.go("/"),
                            ),
                            ft.Container(
                                width=100,
                                margin=ft.margin.only(left=215, right=10, top=20),
                                content=ft.TextButton(
                                    "Login",
                                    style=ft.ButtonStyle(
                                        color=LIGHTBLUE, bgcolor=DEEPBLUE
                                    ),
                                    on_click=lambda _: page.go(Routes.LOGIN.value),
                                ),
                            ),
                        ]
                    ),
                    ft.Container(
                        width=400,
                        margin=ft.margin.only(left=120, right=10, top=30),
                        content=ft.Text(
                            "Criar conta",
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
                        height=550,
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    content=self.profile_image_picker,
                                    margin=ft.margin.only(top=10),
                                ),
                                ft.Container(
                                    width=400,
                                    margin=ft.margin.only(left=20, right=20, top=30),
                                    content=self.name_input,
                                ),
                                ft.Container(
                                    width=400,
                                    margin=ft.margin.only(left=20, right=20, top=15),
                                    content=self.nickname_input,
                                ),
                                ft.Container(
                                    width=400,
                                    margin=ft.margin.only(left=20, right=20, top=15),
                                    content=self.pix_type_dropdown,
                                ),
                                ft.Container(
                                    width=400,
                                    margin=ft.margin.only(left=20, right=20, top=15),
                                    content=self.pix_value_input,
                                ),
                                ft.Container(
                                    width=400,
                                    margin=ft.margin.only(left=20, right=20, top=15),
                                    content=self.phone_number_input,
                                ),
                                ft.Container(
                                    width=400,
                                    margin=ft.margin.only(left=20, right=20, top=15),
                                    content=self.email_input,
                                ),
                                ft.Container(
                                    width=400,
                                    margin=ft.margin.only(left=20, right=20, top=15),
                                    content=self.password_input,
                                ),
                                ft.Container(
                                    width=400,
                                    margin=ft.margin.only(left=20, right=20, top=15),
                                    content=self.confirm_password_input,
                                ),
                            ],
                            scroll=ft.ScrollMode.ADAPTIVE,
                        ),
                    ),
                    ft.Container(
                        width=100,
                        margin=ft.margin.only(left=140, right=20, top=10),
                        content=self.sign_up_button,
                    ),
                ],
            ),
        )
