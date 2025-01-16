import flet as ft

from fazaconta_frontend.src.constants import (
    BORDER_RADIUS,
    MEDIUMBLUE,
    VIEW_HEIGHT,
    VIEW_WIDTH,
    WHITE,
    Routes,
)


class DebtsOrReceivablesView(ft.View):
    page: ft.Page

    def __init__(
        self,
        page: ft.Page,
        title: str,
        total_amount: float,
        details: list,
        is_debt: bool,
    ):

        super().__init__(
            route=Routes.BALANCES,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        self.page = page
        self.title = title
        self.total_amount = total_amount
        self.details = details
        self.is_debt = is_debt
        self.controls = self._build_controls()

    def change_route(self, route: Routes):
        self.page.views.clear()
        self.page.go(Routes.GROUP_DETAILS.value)
        # self.page.update()

        # self.page.go(Routes.GROUP_DETAILS.value)

    def _build_controls(self):
        def total_section():
            """Header showing the total amount owed/receivable."""
            amount_color = ft.colors.RED if self.is_debt else ft.colors.GREEN
            return ft.Container(
                alignment=ft.alignment.center,
                width=VIEW_WIDTH,
                height=VIEW_HEIGHT,
                padding=ft.padding.symmetric(horizontal=25, vertical=20),
                bgcolor=MEDIUMBLUE,
                border_radius=BORDER_RADIUS,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                    controls=[
                        ft.Container(
                            width=VIEW_WIDTH,
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Container(
                                        ft.Icon(
                                            ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                            color=WHITE,
                                        ),
                                        on_click=lambda _: self.change_route(
                                            Routes.GROUP_DETAILS
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        ft.Text(
                            self.title,
                            size=16,
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Container(
                            padding=ft.padding.symmetric(horizontal=20, vertical=8),
                            border_radius=20,
                            bgcolor=amount_color,
                            content=ft.Text(
                                f"R$ {self.total_amount:,.2f}".replace(".", ","),
                                size=20,
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ),
                    ],
                ),
            )

        def detail_card(transaction):
            """Card for an individual transaction."""
            from_user = transaction["from_user"]
            to_user = transaction["to_user"]
            amount = transaction["amount"]
            amount_color = ft.colors.RED if amount < 0 else ft.colors.GREEN
            amount_text = f"R$ {abs(amount):,.2f}".replace(".", ",")

            return ft.Container(
                bgcolor=ft.colors.BLACK26,
                border_radius=15,
                padding=ft.padding.symmetric(horizontal=15, vertical=10),
                margin=ft.margin.only(bottom=10),
                content=ft.Column(
                    spacing=10,
                    controls=[
                        # Title with "Alex deve João" or "Gabi deve Alex"
                        ft.Text(
                            f"{from_user} {'deve' if self.is_debt else 'tem a pagar'} {to_user}",
                            size=16,
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                        ),
                        # Amount
                        ft.Text(
                            amount_text,
                            size=20,
                            color=amount_color,
                            weight=ft.FontWeight.BOLD,
                        ),
                        # Buttons
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                # "Marcar como Pago" button
                                ft.Container(
                                    content=ft.Text(
                                        (
                                            "Marcar como Pago"
                                            if self.is_debt
                                            else "Cobrar"
                                        ),
                                        size=14,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.colors.WHITE,
                                    ),
                                    padding=ft.padding.symmetric(
                                        horizontal=15, vertical=8
                                    ),
                                    border_radius=20,
                                    bgcolor=ft.colors.BLUE,
                                ),
                                # "Convidar" button
                                ft.Container(
                                    content=ft.Text(
                                        "Convidar",
                                        size=14,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.colors.BLACK,
                                    ),
                                    padding=ft.padding.symmetric(
                                        horizontal=15, vertical=8
                                    ),
                                    border_radius=20,
                                    bgcolor=ft.colors.WHITE,
                                ),
                            ],
                        ),
                    ],
                ),
            )

        # Generate detail cards
        detail_cards = [detail_card(detail) for detail in self.details]

        return [
            # Total section
            total_section(),
            # List of detail cards
            ft.Column(controls=detail_cards, spacing=10),
        ]
