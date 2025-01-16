from click import group
import flet as ft
from fazaconta_frontend.src.api.ApiClient import api_client
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
from fazaconta_frontend.src.utils import to_formatted_date, to_money
from fazaconta_frontend.src.views.DebtsOrReceivablesView import DebtsOrReceivablesView


class GroupDetailsView(ft.View):
    page: ft.Page
    is_private: bool

    def __init__(self, page: ft.Page, group_id: str, is_private: bool = False):
        super().__init__(
            route=Routes.GROUP_DETAILS,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        self.page = page
        self.is_private = is_private
        self.selected_tab = "Transações"
        self.token = self.page.client_storage.get("token").get("access_token", None)
        self.me = api_client.me(self.token)
        self.group = api_client.get_group_details(group_id, self.token)
        self.own_expenses = self.calculate_own_expenses()
        self.controls = self._build_controls()

    def calculate_own_expenses(self):
        my_total_expense = 0
        for transaction in self.group.transactions:
            if transaction.transaction_type != "expense":
                continue

            for participant in transaction.participants:
                if participant.user.id == self.me.id:
                    my_total_expense += participant.amount

        return my_total_expense

    def _build_controls(self):

        self.add_transaction = self._build_add_transaction()
        return [
            ft.Container(
                alignment=ft.alignment.center,
                width=VIEW_WIDTH,
                height=VIEW_HEIGHT,
                padding=ft.padding.symmetric(horizontal=25, vertical=20),
                bgcolor=MEDIUMBLUE,
                border_radius=BORDER_RADIUS,
                content=ft.Column(
                    expand=True,
                    controls=[
                        self.header(),
                        self.main(),
                        self.add_transaction,
                    ],
                ),
            )
        ]

    def main(self):
        self.tab_data = ft.Container(content=self.transactions_tab())
        return ft.Column(
            width=VIEW_WIDTH,
            expand=True,
            scroll=ft.ScrollMode.HIDDEN,
            spacing=25,
            controls=[
                self.group_info(),
                self.tabs(),
                self.tab_data,
            ],
        )

    def _build_add_transaction(self):
        fab = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            bgcolor=LIGHTBLUE,
            on_click=lambda _, group_id=self.group.id: self.page.go(
                Routes.CREATE_TRANSACTION.value.replace(":group_id", str(group_id))
            ),
            tooltip="Adicionar transação",
        )

        return ft.Container(
            content=fab,
            alignment=ft.alignment.bottom_center,
            padding=ft.padding.only(bottom=20),
        )

    def transactions_tab(self):
        return ft.Column(
            controls=[
                self.total_expenses(),
                self.transactions(),
            ]
        )

    def transactions(self):
        def expense_card(icon, title, subtitle, amount):
            return ft.Container(
                bgcolor=ft.colors.BLACK12,
                border_radius=8,
                padding=ft.padding.symmetric(horizontal=15, vertical=10),
                content=ft.Row(
                    controls=[
                        ft.Row(
                            spacing=15,
                            controls=[
                                ft.Icon(icon, size=40, color=ft.colors.WHITE),
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            title,
                                            color=ft.colors.WHITE,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Text(
                                            subtitle, color=ft.colors.WHITE54, size=12
                                        ),
                                    ],
                                    spacing=5,
                                ),
                            ],
                        ),
                        ft.Text(
                            amount,
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=18,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            )

        transactions_by_date = ft.Column(spacing=15, controls=[])

        if self.group.transactions is None or len(self.group.transactions) == 0:
            transactions_by_date.controls.append(
                ft.Container(
                    alignment=ft.alignment.center,
                    margin=ft.margin.symmetric(vertical=100),
                    content=ft.Text(
                        "Não existem despesas criadas para o grupo!",
                        text_align=ft.TextAlign.CENTER,
                        size=22,
                    ),
                )
            )
            return transactions_by_date

        transactions = self.group.transactions
        last_formatted_date = to_formatted_date(transactions[0].created_at)
        transactions_by_date.controls.append(
            ft.Text(
                last_formatted_date,
                color=ft.colors.WHITE,
                size=16,
                weight=ft.FontWeight.BOLD,
            ),
        )

        transaction_type_to_name = {
            "send": "Transferido",
            "expense": "Pago",
            "reimbursement": "Reembolsado",
        }

        for transaction in self.group.transactions:
            formatted_date = to_formatted_date(transaction.created_at)
            if formatted_date != last_formatted_date:
                last_formatted_date = to_formatted_date(transaction.created_at)
                transactions_by_date.controls.append(
                    ft.Text(
                        last_formatted_date,
                        color=ft.colors.WHITE,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                    ),
                )

            transactions_by_date.controls.append(
                expense_card(
                    ft.icons.CREDIT_CARD,
                    (
                        transaction.title
                        if transaction.transaction_type != "reimbursement"
                        else "Reembolso"
                    ),
                    f"{transaction_type_to_name.get(transaction.transaction_type, "Pago")} por {transaction.paid_by.nickname}",
                    to_money(transaction.amount),
                ),
            )

        return transactions_by_date

    def total_expenses(self):
        return ft.Container(
            width=VIEW_WIDTH,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=45,
                controls=[
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Minhas Despesas",
                                color=ft.colors.GREY_300,
                                size=12,
                            ),
                            ft.Text(
                                to_money(self.own_expenses),
                                color=ft.colors.WHITE,
                                size=22,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                    ),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Despesas Totais",
                                color=ft.colors.GREY_300,
                                size=12,
                            ),
                            ft.Text(
                                to_money(self.group.total_expense),
                                color=ft.colors.WHITE,
                                size=22,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                    ),
                ],
            ),
        )

    def group_info(self):
        return ft.Container(
            width=VIEW_WIDTH,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                controls=[
                    ft.Container(
                        width=70,
                        height=70,
                        border_radius=35,
                        content=(
                            ft.Image(
                                src=(
                                    str(self.group.image.src)
                                    if self.group.image and self.group.image.src
                                    else None
                                ),
                                fit=ft.ImageFit.COVER,
                            )
                            if self.group.image and self.group.image.src
                            else ft.Icon(ft.icons.MONEY, color=WHITE)
                        ),
                    ),
                    ft.Text(
                        self.group.title,
                        color=WHITE,
                        size=24,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
            ),
        )

    def header(self):
        return ft.Container(
            width=VIEW_WIDTH,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Container(
                        ft.Icon(
                            ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
                            color=WHITE,
                        ),
                        on_click=lambda _: self.page.go(Routes.GROUPS_LIST.value),
                    ),
                    ft.PopupMenuButton(
                        tooltip="Menu",
                        bgcolor=DEEPBLUE,
                        items=[
                            ft.PopupMenuItem(
                                icon=ft.icons.LINK,
                                text="Copiar link",
                            )
                        ],
                        icon_color=WHITE,
                    ),
                ],
            ),
        )

    def balance(self):
        def owed_section(title, amount, subtitle, icon):

            return ft.Container(
                bgcolor=ft.colors.BLACK38,
                border_radius=15,
                on_click=lambda _: self.navigate_to_debts_or_receivables(is_debt=True),
                padding=ft.padding.symmetric(horizontal=15, vertical=10),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            spacing=10,
                            controls=[
                                # Icon for the owed/receiving section
                                ft.Container(
                                    width=40,
                                    height=40,
                                    border_radius=20,
                                    bgcolor=ft.colors.ORANGE_500,
                                    alignment=ft.alignment.center,
                                    content=ft.Text(
                                        icon,
                                        size=18,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ),
                                # Texts
                                ft.Column(
                                    spacing=5,
                                    controls=[
                                        ft.Text(
                                            title,
                                            color=ft.colors.WHITE,
                                            size=14,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Text(
                                            amount,
                                            color=ft.colors.WHITE,
                                            size=12,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Text(
                                            subtitle,
                                            color=ft.colors.GREY_300,
                                            size=12,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        # Right arrow icon
                        ft.Icon(
                            ft.icons.CHEVRON_RIGHT,
                            color=ft.colors.WHITE,
                        ),
                    ],
                ),
            )

        def balance_card(name, balance, is_current_user=False, avatar=None):
            """Helper function to create a balance card for each user."""
            color = ft.colors.RED_500 if balance < 0 else ft.colors.GREEN_400
            balance_text = to_money(balance)

            return ft.Container(
                bgcolor=ft.colors.BLACK38,  # Card background
                border_radius=15,
                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            spacing=15,
                            controls=[
                                ft.Container(
                                    width=40,
                                    height=40,
                                    border_radius=20,
                                    bgcolor=ft.colors.GREY_800,
                                    alignment=ft.alignment.center,
                                    content=(
                                        ft.Text(
                                            name[
                                                0
                                            ],  # Use the first letter as placeholder
                                            color=ft.colors.WHITE,
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            text_align=ft.TextAlign.CENTER,
                                        )
                                        if avatar is None
                                        else ft.Image(src=avatar, fit=ft.ImageFit.COVER)
                                    ),
                                ),
                                # Name and subtitle
                                ft.Column(
                                    spacing=5,
                                    controls=[
                                        ft.Text(
                                            f"{name} {'(Eu)' if is_current_user else ''}",
                                            color=ft.colors.WHITE,
                                            size=16,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        # Balance
                        ft.Text(
                            balance_text,
                            color=color,
                            weight=ft.FontWeight.BOLD,
                            size=16,
                        ),
                    ],
                ),
            )

        balance_cards = [
            balance_card(
                name=m.user.nickname,
                balance=m.balance,
                is_current_user=m.user.id == self.me.id,
            )
            for m in self.group.members
        ]

        owed_payments = [
            p for p in self.group.pending_payments if p.from_user.id == self.me.id
        ]
        receiving_payments = [
            p for p in self.group.pending_payments if p.to_user.id == self.me.id
        ]

        owed_or_receiving_section = []
        if len(owed_payments) > 0:
            owed_or_receiving_section.append(
                owed_section(
                    title="Você tem a pagar",
                    amount=to_money(sum(p.amount for p in owed_payments)),
                    subtitle=f"Veja quanto você precisa pagar para {", ".join(p.to_user.nickname for p in owed_payments)}",
                    icon="💸",
                )
            )

        if len(receiving_payments) > 0:
            owed_or_receiving_section.append(
                owed_section(
                    title="Você tem a receber",
                    amount=to_money(sum(p.amount for p in receiving_payments)),
                    subtitle=f"Veja quanto você tem a receber de {", ".join([p.from_user.nickname for p in receiving_payments])}",
                    icon="💸",
                )
            )
        # owed_or_receiving_section = owed_section(
        #     title="Você tem a receber",
        #     amount="US$ 150,00",
        #     subtitle="Veja quanto Gabi precisa te pagar de volta",
        #     icon="💸",
        # )

        return ft.Container(
            width=VIEW_WIDTH,
            content=ft.Column(
                spacing=20,
                controls=[
                    *owed_or_receiving_section,
                    ft.Text(
                        "Saldos",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                    ),
                    ft.Column(
                        spacing=10, scroll=ft.ScrollMode.HIDDEN, controls=balance_cards
                    ),
                ],
            ),
        )

    def navigate_to_debts_or_receivables(self, is_debt):
        if is_debt:
            # Data for "Você deve"
            title = "Você deve"
            total_amount = 694.25
            details = [
                {"from_user": "Alex", "to_user": "João", "amount": 300.00},
                {"from_user": "Alex", "to_user": "Marta", "amount": 284.75},
                {"from_user": "Alex", "to_user": "Pedro", "amount": 109.50},
            ]
        else:
            # Data for "Você tem a receber"
            title = "Você tem a receber"
            total_amount = 150.00
            details = [
                {"from_user": "Gabi", "to_user": "Alex", "amount": -150.00},
            ]

        # Push the new view
        self.page.views.append(
            DebtsOrReceivablesView(self.page, title, total_amount, details, is_debt)
        )
        self.page.update()

    def tabs(self):
        def set_tab(tab_name):
            self.selected_tab = tab_name

            if self.selected_tab == "Transações":
                self.tab_data.content = self.transactions_tab()
                self.add_transaction.visible = True
            elif self.selected_tab == "Saldos":
                self.tab_data.content = self.balance()
                self.add_transaction.visible = False

            for tab in tabs_row.controls:
                tab_name = tab.data
                if tab_name == self.selected_tab:
                    tab.bgcolor = ft.colors.WHITE
                    tab.content.color = DEEPBLUE
                else:
                    tab.bgcolor = DEEPBLUE
                    tab.content.color = ft.colors.WHITE

            self.update()

        def create_tab(tab_name):
            is_selected = tab_name == self.selected_tab
            return ft.Container(
                content=ft.Text(
                    tab_name,
                    color=ft.colors.BLACK if is_selected else ft.colors.WHITE,
                ),
                bgcolor=ft.colors.WHITE if is_selected else ft.colors.BLACK,
                alignment=ft.alignment.center,
                expand=True,
                height=30,
                data=tab_name,
                on_click=lambda _: set_tab(tab_name),
            )

        tabs_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                create_tab("Transações"),
                create_tab("Saldos"),
            ],
            spacing=0,
        )

        set_tab(self.selected_tab)

        return ft.Container(
            width=VIEW_WIDTH,
            border_radius=25,
            content=ft.Container(border_radius=25, content=tabs_row),
        )
