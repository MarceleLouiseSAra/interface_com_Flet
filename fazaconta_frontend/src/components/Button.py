import flet as ft

from fazaconta_frontend.src.constants import LIGHTBLUE, MEDIUMBLUE, PINK, WHITE


class Button(ft.UserControl):
    def __init__(
        self,
        text,
        on_click,
        default_bg_color=MEDIUMBLUE,
        loading_bg_color=ft.colors.GREY,
        **button_props
    ):
        super().__init__()
        self.default_text = text
        self.on_click_callback = on_click
        self.default_bg_color = default_bg_color
        self.loading_bg_color = loading_bg_color
        self.is_loading = False

        self.button = ft.ElevatedButton(
            text,
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.HOVERED: LIGHTBLUE,
                    ft.ControlState.FOCUSED: WHITE,
                    ft.ControlState.DEFAULT: PINK,
                },
                bgcolor=self.default_bg_color,
            ),
            on_click=self.handle_click,
            **button_props
        )

        self.progress_ring = ft.ProgressRing(width=20, height=20, visible=False)
        self.controls = [
            ft.Row(
                [self.button, self.progress_ring], alignment=ft.MainAxisAlignment.CENTER
            )
        ]

    def handle_click(self, e):
        self.on_click_callback(e)

    def set_loading_state(self, is_loading):
        self.is_loading = is_loading
        self.update_ui()

    def update_ui(self):
        if self.is_loading:
            self.button.text = "Carregando..."
            self.button.disabled = True
            self.button.style.bgcolor = self.loading_bg_color
            self.progress_ring.visible = True
        else:
            self.button.text = self.default_text
            self.button.disabled = False
            self.button.style.bgcolor = self.default_bg_color
            self.progress_ring.visible = False
        self.update()
