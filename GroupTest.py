import flet as ft

from fazaconta_frontend.src.constants import (
    BORDER_RADIUS,
    DEEPBLUE,
    LIGHTBLUE,
    VIEW_HEIGHT,
    VIEW_WIDTH,
    WHITE,
    Routes,
)

group_template = {
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


class GroupDetailsView(ft.View):
    page: ft.Page
    is_private: bool

    def __init__(self, page: ft.Page, is_private: bool = False):
        super().__init__(
            route=Routes.GROUP_DETAILS,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        self.page = page
        self.is_private = is_private
        self.group = group_template

        self.bgcolor = DEEPBLUE
        self.appbar = ft.AppBar(
            bgcolor=DEEPBLUE,
            title=ft.Text("FazAConta"),
            center_title=True,
            leading=ft.Container(
                ft.Icon(
                    ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                    color=LIGHTBLUE,
                ),
                on_click=lambda _: self.page.go(Routes.GROUPS_LIST),
            ),
            actions=[
                ft.PopupMenuButton(
                    items=[ft.PopupMenuItem(icon=ft.icons.LINK, text="Copiar link")]
                )
            ],
        )
        self.add_group_button = ft.Container(
            content=ft.FloatingActionButton(
                icon=ft.icons.ADD,
                bgcolor=LIGHTBLUE,
                on_click=lambda _: self.page.go("/create_group_page"),
                tooltip="Criar Novo Grupo",
            )
        )

        # Floating Action Button
        fab = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            bgcolor=LIGHTBLUE,
            on_click=lambda _: self.page.go("/create_group_page"),
            tooltip="Criar Novo Grupo",
        )

        # Position the FAB at the center bottom with some space from the bottom
        self.add_group_button = ft.Container(
            content=fab,
            alignment=ft.alignment.bottom_center,  # Align at the center bottom
            padding=ft.padding.only(bottom=20),  # Add 20px of space above the bottom
        )

        self.controls = self._build_controls()

        # # Balances
        # balances = ft.Row(
        #     controls=[
        #         ft.Column(
        #             controls=[
        #                 ft.Text("Minhas Despesas", color=ft.colors.WHITE, size=16),
        #                 ft.Text(
        #                     "US$ 876,50",
        #                     color=ft.colors.WHITE,
        #                     size=22,
        #                     weight=ft.FontWeight.BOLD,
        #                 ),
        #             ]
        #         ),
        #         ft.Column(
        #             controls=[
        #                 ft.Text("Despesas Totais", color=ft.colors.WHITE, size=16),
        #                 ft.Text(
        #                     "US$ 1.653,00",
        #                     color=ft.colors.WHITE,
        #                     size=22,
        #                     weight=ft.FontWeight.BOLD,
        #                 ),
        #             ]
        #         ),
        #     ],
        #     alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        # )

        # # Expense Cards
        # def expense_card(icon, title, subtitle, amount, color=ft.colors.BLACK12):
        #     return ft.Container(
        #         bgcolor=color,
        #         border_radius=8,
        #         padding=10,
        #         content=ft.Row(
        #             controls=[
        #                 ft.Icon(icon, size=40),
        #                 ft.Column(
        #                     controls=[
        #                         ft.Text(
        #                             title,
        #                             color=ft.colors.WHITE,
        #                             weight=ft.FontWeight.BOLD,
        #                         ),
        #                         ft.Text(subtitle, color=ft.colors.WHITE54, size=12),
        #                     ],
        #                     spacing=5,
        #                 ),
        #                 ft.Text(
        #                     amount,
        #                     color=ft.colors.WHITE,
        #                     weight=ft.FontWeight.BOLD,
        #                     size=18,
        #                 ),
        #             ],
        #             alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        #         ),
        #     )

        # # Expenses grouped by date
        # expenses_by_date = ft.Column(
        #     controls=[
        #         ft.Text(
        #             "12 de janeiro de 2025",
        #             color=ft.colors.WHITE,
        #             size=16,
        #             weight=ft.FontWeight.BOLD,
        #         ),
        #         expense_card(
        #             ft.icons.CREDIT_CARD,
        #             "Reimbursement",
        #             "Transferido por Gabi",
        #             "US$ 415,00",
        #         ),
        #         ft.Text(
        #             "5 de janeiro de 2025",
        #             color=ft.colors.WHITE,
        #             size=16,
        #             weight=ft.FontWeight.BOLD,
        #         ),
        #         expense_card(
        #             ft.icons.MONEY, "Alow", "Pago por João (eu)", "US$ 300,00"
        #         ),
        #         expense_card(
        #             ft.icons.CREDIT_CARD,
        #             "Opa",
        #             "Transferido por João (eu)",
        #             "US$ 300,00",
        #         ),
        #         ft.Text(
        #             "4 de janeiro de 2025",
        #             color=ft.colors.WHITE,
        #             size=16,
        #             weight=ft.FontWeight.BOLD,
        #         ),
        #         expense_card(ft.icons.MONEY, "B", "Pago por Gabi", "US$ 20,00"),
        #         expense_card(ft.icons.MONEY, "Algo", "Pago por João", "US$ 50,00"),
        #     ],
        #     spacing=15,
        # )

        # # Floating Action Button
        # add_expense_button = ft.FloatingActionButton(
        #     icon=ft.icons.ADD,
        #     text="Adicionar Despesa",
        #     on_click=lambda _: print("Add Expense"),
        # )

    def _build_controls(self):
        return [
            ft.Stack(
                expand=True,
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        # width=VIEW_WIDTH,
                        # height=VIEW_HEIGHT,
                        padding=ft.padding.symmetric(horizontal=20, vertical=20),
                        bgcolor=DEEPBLUE,
                        border_radius=BORDER_RADIUS,
                        content=ft.Column(
                            width=VIEW_WIDTH,
                            spacing=15,
                            controls=[
                                # ft.Container(
                                #     width=VIEW_WIDTH,
                                #     content=ft.Row(
                                #         controls=[
                                #             ft.Container(
                                #                 ft.Icon(
                                #                     ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                #                     color=LIGHTBLUE,
                                #                 ),
                                #                 on_click=lambda _: self.page.go(
                                #                     Routes.GROUPS_LIST
                                #                 ),
                                #             ),
                                #             ft.Container(
                                #                 width=100,
                                #                 content=ft.TextButton(
                                #                     "Login",
                                #                     style=ft.ButtonStyle(
                                #                         color=LIGHTBLUE, bgcolor=DEEPBLUE
                                #                     ),
                                #                     on_click=lambda _: self.page.go(
                                #                         Routes.LOGIN.value
                                #                     ),
                                #                 ),
                                #             ),
                                #         ],
                                #         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                #     ),
                                # ),
                                ft.Container(
                                    width=VIEW_WIDTH,
                                    content=ft.Column(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=15,
                                        controls=[
                                            ft.Container(
                                                width=60,
                                                height=60,
                                                border_radius=30,
                                                content=(
                                                    ft.Image(
                                                        src=(
                                                            self.group["image"]["src"]
                                                            if self.group.get("image")
                                                            and self.group["image"].get(
                                                                "src"
                                                            )
                                                            else None
                                                        ),
                                                        fit=ft.ImageFit.COVER,
                                                    )
                                                    if self.group.get("image")
                                                    and self.group["image"].get("src")
                                                    else ft.Icon(
                                                        ft.icons.MONEY, color=WHITE
                                                    )
                                                ),
                                            ),
                                            ft.Text(
                                                self.group["title"],
                                                color=WHITE,
                                                size=20,
                                            ),
                                        ],
                                    ),
                                ),
                                ft.Container(
                                    border_radius=25,
                                    # content=self.tabs_row,
                                    width=VIEW_WIDTH,
                                    bgcolor=LIGHTBLUE,
                                ),
                                ft.Container(
                                    width=VIEW_WIDTH, height=150, bgcolor=LIGHTBLUE
                                ),
                                ft.Container(
                                    width=VIEW_WIDTH, height=150, bgcolor=LIGHTBLUE
                                ),
                            ],
                        ),
                    ),
                    self.add_group_button,
                ],
            )
        ]

    def _tabs(self):
        self.selected_tab = "Despesas"

        def set_tab(self, tab_name):
            self.selected_tab = tab_name
            self.update()

        def on_tab_click(self, tab_name):
            self.set_tab(tab_name)

        # "Selected" tab: White background and black text
        tab_despesas = ft.Container(
            content=ft.Text("Despesas", color=ft.colors.BLACK),
            bgcolor=ft.colors.WHITE,
            alignment=ft.alignment.center,
            width=120,
            height=40,
            # border_radius=ft.border_radius.all(3),
        )

        # "Unselected" tabs: Black background and white text
        tab_saldos = ft.Container(
            content=ft.Text("Saldos", color=ft.colors.WHITE),
            bgcolor=ft.colors.BLACK,
            alignment=ft.alignment.center,
            width=120,
            height=40,
            # border_radius=ft.border_radius.all(3),
        )

        tab_fotos = ft.Container(
            content=ft.Text("Fotos", color=ft.colors.WHITE),
            bgcolor=ft.colors.BLACK,
            alignment=ft.alignment.center,
            width=120,
            height=40,
            # on_click=on_click,
            # border_radius=ft.border_radius.all(3),
        )

        # Place the 3 tab containers in a single row
        self.tabs_row = ft.Row(
            controls=[tab_despesas, tab_saldos, tab_fotos],
            spacing=0,
        )
