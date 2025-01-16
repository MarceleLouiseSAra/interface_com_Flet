import flet as ft
from fazaconta_frontend.src.api.ApiClient import api_client
from fazaconta_frontend.src.constants import VIEW_WIDTH, Routes

DEEPBLUE = "#432350"
MEDIUMBLUE = "#b476ff"
PINK = "#f4c9fd"
WHITE = "#ffffff"
LIGHTBLUE = "#B0C4DE"


groups_template = [
    {
        "id": "9fb1f2e4-613c-4142-9d52-d5ad979a8ef0",
        "title": "Bebidas",
        "created_by": {
            "id": "dfed7a69-f7f8-4319-bec4-6a349c57308d",
            "name": "João Pedro Lima Pirajá",
            "nickname": "Pirajá",
            "email": "jplp100@hotmail.com",
            "phone_number": "71999258225",
            "profile_photo": {
                "key": "d533a122-6294-472e-a538-df3d0ce444b2_moon-sunset-horizon-1920x1080-15494.jpg",
                "src": "http://0.0.0.0:8000/files/d533a122-6294-472e-a538-df3d0ce444b2_moon-sunset-horizon-1920x1080-15494.jpg",
                "size": 396187,
                "filename": "moon-sunset-horizon-1920x1080-15494.jpg",
                "content_type": "application/jpg",
            },
            "pix": {"type": "cpf_cnpj", "value": "86231101533"},
        },
        "total_expense": 3500.0,
        "created_at": "2025-01-12T10:35:26.429000",
        "members": [
            {
                "id": "dd1884e0-fd79-4d5c-8790-1ffb5137e9d3",
                "user": {
                    "id": "5e4b5a7f-d862-428c-80b2-a853d133cba5",
                    "name": "Gabrielli Valelia",
                    "nickname": "Gabi",
                    "email": "gabriellisilva1102@gmail.com",
                    "phone_number": "28999348537",
                    "profile_photo": {
                        "key": "f5a60d5a-872e-4b07-aa1f-a469e009d611_moon-sunset-horizon-1920x1080-15494.jpg",
                        "src": "http://0.0.0.0:8000/files/f5a60d5a-872e-4b07-aa1f-a469e009d611_moon-sunset-horizon-1920x1080-15494.jpg",
                        "size": 396187,
                        "filename": "moon-sunset-horizon-1920x1080-15494.jpg",
                        "content_type": "application/jpg",
                    },
                    "pix": {"type": "email", "value": "gabriellisilva1102@gmail.com"},
                },
                "balance": -100.0,
            },
            {
                "id": "e5bbadb8-6f9a-489d-8730-f4730e746cac",
                "user": {
                    "id": "dfed7a69-f7f8-4319-bec4-6a349c57308d",
                    "name": "João Pedro Lima Pirajá",
                    "nickname": "Pirajá",
                    "email": "jplp100@hotmail.com",
                    "phone_number": "71999258225",
                    "profile_photo": {
                        "key": "d533a122-6294-472e-a538-df3d0ce444b2_moon-sunset-horizon-1920x1080-15494.jpg",
                        "src": "http://0.0.0.0:8000/files/d533a122-6294-472e-a538-df3d0ce444b2_moon-sunset-horizon-1920x1080-15494.jpg",
                        "size": 396187,
                        "filename": "moon-sunset-horizon-1920x1080-15494.jpg",
                        "content_type": "application/jpg",
                    },
                    "pix": {"type": "cpf_cnpj", "value": "86231101533"},
                },
                "balance": 100.0,
            },
        ],
        "pending_payments": [
            {
                "id": "ccba9b70-5bc2-4167-a762-9992ddbb1ba7",
                "from_user": {
                    "id": "5e4b5a7f-d862-428c-80b2-a853d133cba5",
                    "name": "Gabrielli Valelia",
                    "nickname": "Gabi",
                    "email": "gabriellisilva1102@gmail.com",
                    "phone_number": "28999348537",
                    "profile_photo": {
                        "key": "f5a60d5a-872e-4b07-aa1f-a469e009d611_moon-sunset-horizon-1920x1080-15494.jpg",
                        "src": "http://0.0.0.0:8000/files/f5a60d5a-872e-4b07-aa1f-a469e009d611_moon-sunset-horizon-1920x1080-15494.jpg",
                        "size": 396187,
                        "filename": "moon-sunset-horizon-1920x1080-15494.jpg",
                        "content_type": "application/jpg",
                    },
                    "pix": {"type": "email", "value": "gabriellisilva1102@gmail.com"},
                },
                "to_user": {
                    "id": "dfed7a69-f7f8-4319-bec4-6a349c57308d",
                    "name": "João Pedro Lima Pirajá",
                    "nickname": "Pirajá",
                    "email": "jplp100@hotmail.com",
                    "phone_number": "71999258225",
                    "profile_photo": {
                        "key": "d533a122-6294-472e-a538-df3d0ce444b2_moon-sunset-horizon-1920x1080-15494.jpg",
                        "src": "http://0.0.0.0:8000/files/d533a122-6294-472e-a538-df3d0ce444b2_moon-sunset-horizon-1920x1080-15494.jpg",
                        "size": 396187,
                        "filename": "moon-sunset-horizon-1920x1080-15494.jpg",
                        "content_type": "application/jpg",
                    },
                    "pix": {"type": "cpf_cnpj", "value": "86231101533"},
                },
                "amount": 100.0,
            }
        ],
        "image": {
            "key": "6f43186c-3c9e-46aa-b9f2-a03545869bd7_moon-sunset-horizon-1920x1080-15494.jpg",
            "src": "http://0.0.0.0:8000/files/6f43186c-3c9e-46aa-b9f2-a03545869bd7_moon-sunset-horizon-1920x1080-15494.jpg",
            "size": 396187,
            "filename": "moon-sunset-horizon-1920x1080-15494.jpg",
            "content_type": "application/jpg",
        },
    }
]


class GroupsListView(ft.View):
    page: ft.Page
    is_private: bool
    is_sidebar_open: bool = False

    def __init__(self, page: ft.Page, is_private: bool = False):
        super().__init__(
            route=Routes.GROUPS_LIST,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        self.page = page
        self.is_private = is_private
        self.token = self.page.client_storage.get("token").get("access_token", None)
        self.me = api_client.me(self.token)
        self.groups = api_client.get_groups(self.token)
        self.filtered_groups = self.groups
        self._build_controls()

    def _build_controls(self):
        self.search_input = ft.TextField(
            hint_text="Pesquisar grupos...",
            on_change=self._filter_groups,
            border_color=LIGHTBLUE,
            focused_border_color=PINK,
        )
        self.group_cards = self._build_group_cards()
        self.main_page = self._build_main_page()
        self.side_bar = self._build_side_bar()
        self.circle = self._build_circle()
        self.profile_content = self._build_profile_content()
        self.home_page = self._build_home_page()

        self.controls = [self.home_page]

    def _build_home_page(self):
        return ft.Container(
            width=400,
            height=850,
            bgcolor=DEEPBLUE,
            border_radius=20,
            margin=ft.margin.only(bottom=20),  # Adds space from bottom
            content=ft.Stack(
                alignment=ft.alignment.bottom_center,
                controls=[
                    self.profile_content,
                    self.side_bar,
                    ft.Container(
                        height=80,
                        width=80,
                        content=ft.FloatingActionButton(
                            icon=ft.icons.ADD,
                            bgcolor=LIGHTBLUE,
                            on_click=lambda _: self.page.go(Routes.CREATE_GROUP.value),
                            tooltip="Criar Novo Grupo",
                        ),
                        padding=15,
                    ),
                ],
            ),
        )

    def _build_side_bar(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.END,
            controls=[
                ft.Container(
                    width=400,
                    height=850,
                    bgcolor=MEDIUMBLUE,
                    border_radius=20,
                    animate=ft.animation.Animation(600, ft.AnimationCurve.DECELERATE),
                    animate_scale=ft.animation.Animation(
                        400, curve=ft.AnimationCurve.DECELERATE
                    ),
                    padding=ft.padding.only(top=50, left=20, right=20, bottom=5),
                    content=ft.Column(controls=[self.main_page]),
                )
            ],
        )

    def _build_main_page(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Container(
                                content=ft.Icon(ft.icons.MENU, color=WHITE),
                                on_click=lambda e: self._move_sibebar(),
                            ),
                            ft.Row(
                                controls=[
                                    # self.search_input,
                                    ft.Container(ft.Icon(ft.icons.SEARCH, color=WHITE)),
                                    ft.Container(
                                        ft.Icon(
                                            ft.icons.NOTIFICATIONS_OUTLINED, color=WHITE
                                        ),
                                    ),
                                ]
                            ),
                        ],
                    ),
                    ft.Text(
                        value="FazAConta",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=WHITE,
                    ),
                    ft.Container(
                        width=400,
                        height=625,
                        content=self.group_cards,
                    ),
                ]
            )
        )

    def _build_group_cards(self):
        if not self.filtered_groups:
            return ft.Container(
                height=400,
                alignment=ft.alignment.center,
                content=ft.Text(
                    "Você ainda não possui grupos.\nCrie um novo grupo clicando no botão '+' abaixo.",
                    size=16,
                    color=LIGHTBLUE,
                    text_align=ft.TextAlign.CENTER,
                ),
            )

        group_cards = ft.Column(scroll=ft.ScrollMode.ADAPTIVE, controls=[])
        for group in self.filtered_groups:
            group_cards.controls.append(
                ft.Container(
                    height=70,
                    width=400,
                    bgcolor=DEEPBLUE,
                    border_radius=10,
                    padding=ft.padding.symmetric(horizontal=20),
                    on_click=lambda _, group_id=group.id: self.page.go(
                        Routes.GROUP_DETAILS.replace(":id", str(group_id))
                    ),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        width=40,
                                        height=40,
                                        border_radius=20,
                                        bgcolor=LIGHTBLUE,
                                        content=(
                                            ft.Image(
                                                src=(str(group.image_src)),
                                                fit=ft.ImageFit.COVER,
                                            )
                                            if group.image_src
                                            else ft.Icon(ft.icons.MONEY, color=WHITE)
                                        ),
                                    ),
                                    ft.Text(group.title, color=WHITE, size=16),
                                ]
                            ),
                            ft.Icon(ft.icons.ARROW_FORWARD, color=WHITE),
                        ],
                    ),
                )
            )
        return group_cards

    def show_snackbar(self, message, color=ft.colors.RED):
        snackbar = ft.SnackBar(ft.Text(message), bgcolor=color)
        self.page.snack_bar = snackbar
        self.page.snack_bar.open = True
        self.page.update()

    def on_logout_error(self, message: str, exc: Exception):
        print(f"Erro ao sair da conta: {message}")
        self.show_snackbar(message, color=ft.colors.RED)

    def logout(self):
        api_client.logout(self.token, on_error=self.on_logout_error)
        self.page.client_storage.remove("token")
        self.page.go(Routes.LOGIN.value)

    def _build_profile_content(self):
        return ft.Container(
            width=VIEW_WIDTH,
            height=850,
            bgcolor=DEEPBLUE,
            border_radius=35,
            padding=ft.padding.only(left=50, top=60, right=200),
            content=ft.Column(
                controls=[
                    ft.Container(
                        animate=ft.animation.Animation(
                            600, ft.AnimationCurve.DECELERATE
                        ),
                        animate_scale=ft.animation.Animation(
                            400, curve=ft.AnimationCurve.DECELERATE
                        ),
                    ),
                    ft.Stack(
                        controls=[
                            ft.FloatingActionButton(
                                icon=ft.icons.HOME,
                                on_click=lambda e: self._move_sibebar(),
                                bgcolor=LIGHTBLUE,
                            ),
                        ]
                    ),
                    ft.Container(height=20),
                    self.circle,
                    ft.Text(
                        self.me.nickname,
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color=LIGHTBLUE,
                    ),
                    ft.Container(height=5),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Icon(
                                                ft.icons.ACCOUNT_CIRCLE_ROUNDED,
                                                color=LIGHTBLUE,
                                            ),
                                        ),
                                        ft.Text(
                                            "Minha conta",
                                            color=LIGHTBLUE,
                                            weight=ft.FontWeight.W_300,
                                            font_family="poppins",
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Icon(
                                                ft.icons.ADMIN_PANEL_SETTINGS_ROUNDED,
                                                color=LIGHTBLUE,
                                            ),
                                            on_click=lambda _: self.page.go("/"),
                                        ),
                                        ft.Text(
                                            "Configurações",
                                            color=LIGHTBLUE,
                                            weight=ft.FontWeight.W_300,
                                            font_family="poppins",
                                        ),
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Icon(
                                                ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                                color=LIGHTBLUE,
                                            ),
                                        ),
                                        ft.Container(
                                            on_click=lambda _: self.logout(),
                                            content=ft.Text(
                                                "Sair da conta",
                                                color=LIGHTBLUE,
                                                weight=ft.FontWeight.W_300,
                                                font_family="poppins",
                                            ),
                                        ),
                                    ]
                                ),
                            ]
                        )
                    ),
                ]
            ),
        )

    def _build_circle(self):
        return ft.Stack(
            controls=[
                ft.Container(
                    width=100, height=100, border_radius=50, bgcolor=LIGHTBLUE
                ),
                ft.Container(
                    gradient=ft.SweepGradient(
                        center=ft.alignment.center,
                        start_angle=0.0,
                        end_angle=3,
                        stops=[0.5, 0.5],
                        colors=["#00000000", PINK],
                    ),
                    width=100,
                    height=100,
                    border_radius=50,
                    content=ft.Row(
                        alignment="center",
                        controls=[
                            ft.Container(
                                padding=ft.padding.all(5),
                                bgcolor=DEEPBLUE,
                                width=90,
                                height=90,
                                border_radius=50,
                                content=ft.Container(
                                    bgcolor=MEDIUMBLUE,
                                    height=80,
                                    width=80,
                                    border_radius=40,
                                    content=ft.CircleAvatar(
                                        opacity=0.8,
                                        foreground_image_url=self.me.profile_photo.src,
                                    ),
                                ),
                            )
                        ],
                    ),
                ),
            ]
        )

    def _move_sibebar(self):
        if self.is_sidebar_open:
            self._restore_sidebar()
        else:
            self._shrink_sidebar()

    def _shrink_sidebar(self):
        self.side_bar.controls[0].width = 200
        self.side_bar.controls[0].scale = ft.transform.Scale(
            0.8, alignment=ft.alignment.center_right
        )
        self.side_bar.controls[0].border_radius = ft.border_radius.only(
            top_left=20, top_right=0, bottom_left=20, bottom_right=0
        )
        self.side_bar.update()
        self.is_sidebar_open = True

    def _restore_sidebar(self):
        self.side_bar.controls[0].width = 400
        self.side_bar.controls[0].scale = ft.transform.Scale(
            1, alignment=ft.alignment.center_right
        )
        self.side_bar.controls[0].border_radius = 20
        self.side_bar.update()
        self.is_sidebar_open = False

    def _filter_groups(self, e):
        search_text = e.control.value.lower()
        self.filtered_groups = [
            group for group in self.groups if search_text in group.title.lower()
        ]
        self.group_cards = self._build_group_cards()
        self.group_cards.update()
