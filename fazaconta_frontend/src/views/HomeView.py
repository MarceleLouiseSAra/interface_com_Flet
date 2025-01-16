import flet as ft
from fazaconta_frontend.src.constants import (
    BORDER_RADIUS,
    DEEPBLUE,
    LIGHTBLUE,
    MEDIUMBLUE,
    VIEW_HEIGHT,
    VIEW_WIDTH,
    WHITE,
    Routes,
)
from fazaconta_frontend.src.utils import is_authenticated


class HomeView(ft.View):
    page: ft.Page
    is_private: bool

    def __init__(self, page: ft.Page, is_private: bool = False):
        super().__init__(
            route=Routes.HOME,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        self.page = page
        self.is_private = is_private
        self.controls = [self._main_content(page)]

    def did_mount(self):
        super().did_mount()
        if is_authenticated(self.page):
            self.page.go(Routes.GROUPS_LIST)

    def _main_content(self, page: ft.Page):
        return ft.Container(
            width=VIEW_WIDTH,
            height=VIEW_HEIGHT,
            bgcolor=DEEPBLUE,
            border_radius=BORDER_RADIUS,
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            value="FazAConta",
                            size=48,
                            weight=ft.FontWeight.BOLD,
                            color=LIGHTBLUE,
                        ),
                    ),
                    ft.Container(height=200),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                width=150,
                                content=ft.TextButton(
                                    "Criar conta",
                                    style=ft.ButtonStyle(
                                        bgcolor=MEDIUMBLUE,
                                        color={
                                            ft.ControlState.HOVERED: WHITE,
                                            ft.ControlState.FOCUSED: MEDIUMBLUE,
                                            ft.ControlState.DEFAULT: DEEPBLUE,
                                        },
                                    ),
                                    on_click=lambda _: page.go(Routes.REGISTER.value),
                                ),
                            ),
                            ft.Container(
                                width=150,
                                content=ft.TextButton(
                                    "Entrar",
                                    style=ft.ButtonStyle(
                                        bgcolor=MEDIUMBLUE,
                                        color={
                                            ft.ControlState.HOVERED: WHITE,
                                            ft.ControlState.FOCUSED: MEDIUMBLUE,
                                            ft.ControlState.DEFAULT: DEEPBLUE,
                                        },
                                    ),
                                    on_click=lambda _: page.go(Routes.LOGIN.value),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )
