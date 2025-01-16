import flet as ft
from fazaconta_frontend.src.components.Button import Button
from fazaconta_frontend.src.components.Input import Input
from fazaconta_frontend.src.components.CustomCheckBox import CustomCheckBox
from fazaconta_frontend.src.constants import (
    DEEPBLUE,
    MEDIUMBLUE,
    PINK,
    WHITE,
    LIGHTBLUE,
    VIEW_HEIGHT,
    VIEW_WIDTH,
    Routes,
)


class AddTransactionView(ft.View):
    page: ft.Page
    group_id: str
    is_private: bool

    def __init__(self, page: ft.Page, group_id: str, is_private: bool = False):
        super().__init__(
            route=Routes.CREATE_TRANSACTION.value,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )
        self.page = page
        self.group_id = group_id
        self.is_private = is_private
        self.selected_tab = "Despesa"
        self.participants = ["João (eu)", "Marcele", "Caio", "Maria"]  # Fetch from db
        self.amount_per_participant = {
            participant: 0 for participant in self.participants
        }
        self.selected_participants = {
            participant: True for participant in self.participants
        }
        self.controls = [self._main_content()]

    def _main_content(self):
        return ft.Container(
            alignment=ft.alignment.center,
            width=VIEW_WIDTH,
            height=VIEW_HEIGHT,
            bgcolor=DEEPBLUE,
            border_radius=20,
            padding=15,
            content=ft.Column(
                spacing=20,
                controls=[
                    self._header(),
                    self._tabs(),
                    self._form(),
                    self._participants_summary(),
                    self._add_button(),
                ],
            ),
        )

    def _header(self):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        ft.Icon(ft.icons.ARROW_BACK_IOS_NEW_ROUNDED, color=LIGHTBLUE),
                        on_click=lambda _: self.page.go(Routes.GROUP_DETAILS.value),
                    ),
                    ft.Text(
                        "Adicionar Transação",
                        size=20,
                        color=LIGHTBLUE,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            )
        )

    def _tabs(self):
        def set_tab(tab_name):
            self.selected_tab = tab_name
            self.update()

        def create_tab(tab_name):
            is_selected = tab_name == self.selected_tab
            return ft.Container(
                content=ft.Text(
                    tab_name,
                    color=MEDIUMBLUE if is_selected else LIGHTBLUE,
                ),
                bgcolor=WHITE if is_selected else DEEPBLUE,
                alignment=ft.alignment.center,
                expand=True,
                height=40,
                border_radius=10,
                on_click=lambda _: set_tab(tab_name),
            )

        return ft.Row(
            controls=[
                create_tab("Despesa"),
                create_tab("Renda"),
                create_tab("Transferir"),
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def _form(self):
        title_input = Input(
            label="Título",
            hint_text="Ex. Bebidas",
            border_color=MEDIUMBLUE,
            text_style=ft.TextStyle(color=LIGHTBLUE),
            focused_border_color=PINK,
            validation_fn=lambda _: True,
        )

        amount_input = Input(
            label="Valor",
            hint_text="R$ 0,00",
            border_color=MEDIUMBLUE,
            text_style=ft.TextStyle(color=LIGHTBLUE),
            focused_border_color=PINK,
            validation_fn=self._update_amounts,
        )

        paid_by_dropdown = ft.Dropdown(
            label="Pago por",
            options=[
                ft.dropdown.Option(participant) for participant in self.participants
            ],
            border_color=MEDIUMBLUE,
            focused_border_color=PINK,
        )

        when_input = ft.DatePicker(
            # label="Quando",
            # border_color=MEDIUMBLUE,
            # text_style=ft.TextStyle(color=LIGHTBLUE),
            # focused_border_color=PINK,
        )

        participants_checkboxes = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Checkbox(
                            label=participant,
                            value=self.selected_participants[participant],
                            on_change=lambda e, p=participant: self._toggle_participant(
                                p, e.control.value
                            ),
                        )
                    ]
                )
                for participant in self.participants
            ],
        )

        return ft.Column(
            controls=[
                title_input,
                amount_input,
                ft.Row(
                    controls=[
                        ft.Container(content=paid_by_dropdown, expand=1),
                        ft.Container(content=when_input, expand=1),
                    ],
                    spacing=10,
                ),
                participants_checkboxes,
            ],
            spacing=15,
        )

    def _participants_summary(self):
        participant_rows = []

        for participant, amount in self.amount_per_participant.items():
            if self.selected_participants[participant]:
                participant_rows.append(
                    ft.Row(
                        controls=[
                            ft.Text(participant, color=LIGHTBLUE, size=14),
                            ft.Text(f"R$ {amount:.2f}", color=LIGHTBLUE, size=14),
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    )
                )

        return ft.Container(
            content=ft.Column(
                controls=participant_rows,
                spacing=10,
            ),
            margin=ft.margin.only(top=20),
        )

    def _add_button(self):
        return ft.Container(
            content=Button(
                "Adicionar",
                on_click=self._on_add,
            ),
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20),
        )

    def _update_amounts(self, amount_str):
        try:
            total_amount = float(amount_str.replace("R$", "").replace(",", "."))
            active_participants = [
                p for p, selected in self.selected_participants.items() if selected
            ]
            split_amount = total_amount / len(active_participants)
            self.amount_per_participant = {
                participant: (
                    split_amount if self.selected_participants[participant] else 0
                )
                for participant in self.participants
            }
            self.update()
        except ValueError:
            pass

    def _toggle_participant(self, participant, is_selected):
        self.selected_participants[participant] = is_selected
        self._update_amounts("R$ 0.00")

    def _on_add(self, e):
        self.page.snack_bar = ft.SnackBar(
            ft.Text("Transação adicionada com sucesso!"), bgcolor=MEDIUMBLUE
        )
        self.page.snack_bar.open = True
        self.page.update()
