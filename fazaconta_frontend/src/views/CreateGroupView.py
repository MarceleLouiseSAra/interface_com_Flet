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


class CreateGroupView(ft.View):
    page: ft.Page
    is_private: bool
    title_input: Input
    group_image_path: str | None

    def __init__(self, page: ft.Page, is_private: bool = False):
        super().__init__(
            route=Routes.CREATE_GROUP,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        self.page = page
        self.is_private = is_private

        self.group_image_path = None
        self.profile_image_picker = ProfileImagePicker(
            page=self.page,
            on_image_change=self.on_profile_image_selected,
            tooltip_message="Modificar imagem do grupo",
        )

        self.title_input = Input(
            label="Título do grupo",
            hint_text="Insira aqui o título do grupo",
            border_color=MEDIUMBLUE,
            text_style=ft.TextStyle(color=LIGHTBLUE),
            focused_border_color=PINK,
            validation_fn=self.validate_name,
        )

        self.sign_up_button = Button("Criar grupo", on_click=self.on_submit)
        self.controls = [self._main_content(page)]

    def on_profile_image_selected(self, image_path):
        self.group_image_path = image_path

    def validate_name(self, name):
        if not name:
            return "O título do grupo é obrigatório."
        if len(name) < 3:
            return "O título do grupo deve ter pelo menos 3 caracteres."
        return None

    def show_snackbar(self, message, color=ft.colors.RED):
        snackbar = ft.SnackBar(ft.Text(message), bgcolor=color)
        self.page.snack_bar = snackbar
        self.page.snack_bar.open = True
        self.page.update()

    def on_sign_up_success(self, data):
        self.show_snackbar("Grupo criado com sucesso!", color=ft.colors.GREEN)
        self.page.go(Routes.LOGIN.value)

    def on_sign_up_error(self, message: str, exc: Exception):
        print(f"Erro na criação do grupo: {message}")
        self.show_snackbar(message, color=ft.colors.RED)

    def on_submit(self, e):
        name_valid = self.title_input.validate()

        if not name_valid:
            return

        self.sign_up_button.set_loading_state(True)

        token = self.page.client_storage.get("token").get("access_token", None)
        api_client.create_group(
            title=self.title_input.value,
            image_path=self.group_image_path,
            token=token,
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
                width=VIEW_WIDTH,
                controls=[
                    ft.Container(
                        width=VIEW_WIDTH,
                        padding=20,
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    ft.Icon(
                                        ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                        color=LIGHTBLUE,
                                    ),
                                    on_click=lambda _: self.page.go(
                                        Routes.GROUPS_LIST.value
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                    ),
                    ft.Container(
                        width=VIEW_WIDTH,
                        margin=ft.margin.only(left=120, right=10, top=30),
                        content=ft.Text(
                            "Criar Grupo",
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
                                    content=self.title_input,
                                ),
                            ],
                            scroll=ft.ScrollMode.HIDDEN,
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
