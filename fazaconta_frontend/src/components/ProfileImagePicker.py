import flet as ft


class ProfileImagePicker(ft.UserControl):
    def __init__(self, page: ft.Page, on_image_change):
        super().__init__()
        self.page = page
        self.on_image_change = on_image_change
        self.selected_image_path = None

    def build(self):
        self.image_container = ft.Container(
            width=120,
            height=120,
            border_radius=60,  # Ensures the container is circular
            bgcolor=ft.colors.LIGHT_BLUE_100,
            alignment=ft.alignment.center,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,  # Clip the image within circular bounds
            content=ft.Icon(ft.icons.PERSON, size=60, color=ft.colors.WHITE),
        )

        self.file_picker = ft.FilePicker(on_result=self._on_file_picked)
        self.page.overlay.append(self.file_picker)

        return ft.Column(
            controls=[
                ft.Stack(
                    controls=[
                        self.image_container,
                        # Improved edit icon UI
                        ft.Container(
                            width=40,
                            height=40,
                            border_radius=20,  # Circular background for the icon
                            bgcolor=ft.colors.WHITE,
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(right=10, bottom=10),
                            content=ft.IconButton(
                                icon=ft.icons.EDIT,
                                icon_color=ft.colors.BLUE,
                                icon_size=20,
                                tooltip="Modificar imagem de perfil",
                                on_click=lambda _: self.file_picker.pick_files(
                                    allow_multiple=False,
                                    allowed_extensions=["jpg", "jpeg", "png"],
                                ),
                            ),
                        ),
                    ],
                    width=120,
                    height=120,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def _on_file_picked(self, e: ft.FilePickerResultEvent):
        if e.files and e.files[0].path:
            self.selected_image_path = e.files[0].path
            self.image_container.content = ft.Image(
                src=self.selected_image_path,
                width=120,
                height=120,
                fit=ft.ImageFit.COVER,  # Ensures the image fills the circular container
            )
            self.image_container.update()
            if self.on_image_change:
                self.on_image_change(self.selected_image_path)
