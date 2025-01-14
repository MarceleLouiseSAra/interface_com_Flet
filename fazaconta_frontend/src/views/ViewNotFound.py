import flet as ft

from fazaconta_frontend.src.constants import (
    BORDER_RADIUS,
    DEEPBLUE,
    MEDIUMBLUE,
    VIEW_HEIGHT,
    VIEW_WIDTH,
    WHITE,
)


class ViewNotFound(ft.View):
    is_private: bool

    def __init__(self, page: ft.Page, is_private: bool = False):
        super().__init__(
            route="/404",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        self.controls = [self._main_content(page)]
        self.is_private = is_private

    def _main_content(self, page: ft.Page):
        return ft.Container(
            width=VIEW_WIDTH,
            height=VIEW_HEIGHT,
            bgcolor=DEEPBLUE,
            border_radius=BORDER_RADIUS,
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "404 - Página não encontrada",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.TextButton(
                        "Retornar",
                        style=ft.ButtonStyle(
                            bgcolor=MEDIUMBLUE,
                            color={
                                ft.ControlState.HOVERED: WHITE,
                                ft.ControlState.FOCUSED: MEDIUMBLUE,
                                ft.ControlState.DEFAULT: DEEPBLUE,
                            },
                        ),
                        on_click=lambda _: page.go("/"),
                    ),
                ],
            ),
        )
