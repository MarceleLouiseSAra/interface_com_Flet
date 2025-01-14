import flet as ft


class Input(ft.UserControl):
    def __init__(
        self,
        label,
        hint_text,
        border_color,
        text_style,
        focused_border_color,
        validation_fn,
        **field_props
    ):
        super().__init__()
        self.validation_fn = validation_fn
        self.default_border_color = border_color
        self.error_border_color = ft.colors.RED

        self.input_field = ft.TextField(
            label=label,
            hint_text=hint_text,
            border_color=self.default_border_color,
            text_style=text_style,
            focused_border_color=focused_border_color,
            on_change=self.on_change,
            **field_props
        )
        self.error_message = ft.Text("", color=ft.colors.RED, size=12, visible=False)
        self.controls = [ft.Column(controls=[self.input_field, self.error_message])]

    def validate(self):
        value = self.input_field.value.strip() if self.input_field.value else ""
        error = self.validation_fn(value)
        if error:
            self.error_message.visible = True
            self.error_message.value = error
            self.input_field.border_color = self.error_border_color
            self.update()
            return False
        self.error_message.value = ""
        self.input_field.border_color = self.default_border_color
        self.update()
        return True

    def on_change(self, e):
        if self.error_message.value:
            self.error_message.visible = False
            self.error_message.value = ""
            self.input_field.border_color = self.default_border_color
            self.update()

    @property
    def value(self):
        return self.input_field.value.strip() if self.input_field.value else ""
