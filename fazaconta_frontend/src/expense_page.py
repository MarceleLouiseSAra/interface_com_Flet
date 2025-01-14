from flet import *
from .custom_checkbox import CustomCheckBox

DEEPBLUE = "#432350"
MEDIUMBLUE = "#b476ff"
PINK = "#f4c9fd"
WHITE = "#ffffff"
LIGHTBLUE = "#B0C4DE"

page: Page

despesas = ["pizza", "compras", "uber"]  # puxar do db
participants = ["joão", "marcele", "caio", "maria"]  # puxar do db


def view_expense_page(page: Page) -> Container:

    submit_button = Container(
        content=Column(
            controls=[
                Stack(
                    controls=[
                        FloatingActionButton(
                            top=300,
                            left=150,
                            icon=icons.ADD,
                            on_click=lambda _: page.go("/add_expense_page"),
                            bgcolor=LIGHTBLUE,
                        )
                    ]
                )
            ]
        )
    )

    listaDeDespesas = Column(
        height=130,
        scroll="auto",
    )

    for despesa in despesas:
        listaDeDespesas.controls.append(
            Container(
                margin=margin.only(left=15, right=10, top=5),
                width=320,
                height=70,
                bgcolor=PINK,
                border_radius=10,
                padding=15,
                content=Row(
                    controls=[
                        Text(despesa, size=16, color=DEEPBLUE, weight="w700"),
                        Text(
                            "R$ " + "100,00",  # puxar do db
                            size=16,
                            color=DEEPBLUE,
                            weight="w700",
                        ),
                    ],
                    alignment="spaceBetween",
                ),
            )
        )

    expenses_layer = Container(
        width=350,
        height=300,
        bgcolor=MEDIUMBLUE,
        border_radius=10,
        padding=15,
        content=Column(
            controls=[
                Container(
                    bgcolor=LIGHTBLUE,
                    border_radius=10,
                    padding=15,
                    content=Text(
                        "Total gasto",
                        size=16,
                        weight="w700",
                        color=DEEPBLUE,
                    ),
                ),
                Row(
                    [
                        Container(
                            margin=margin.only(left=120, right=10, top=10),
                            content=Text(
                                "R$ "
                                + "100,00",  # puxar do db (soma do custo de todas as despesas)
                                size=20,
                                color=WHITE,
                                weight="w700",
                            ),
                        ),
                    ]
                ),
                listaDeDespesas,
            ],
            horizontal_alignment=CrossAxisAlignment.START,
        ),
    )

    listaDeParticipantes = Column(
        height=180,
        scroll="auto",
    )

    for participant in participants:
        listaDeParticipantes.controls.append(
            Container(
                margin=margin.only(left=15, right=10, top=5),
                width=320,
                height=70,
                bgcolor=PINK,
                border_radius=10,
                padding=15,
                content=Row(
                    controls=[
                        Text(participant, size=16, color=DEEPBLUE, weight="w700"),
                        Text(
                            "R$ " + "100,00",  # puxar do db
                            size=16,
                            color=DEEPBLUE,
                            weight="w700",
                        ),
                    ],
                    alignment="spaceBetween",
                ),
            )
        )

    balance_layer = Container(
        width=350,
        height=300,
        bgcolor=MEDIUMBLUE,
        border_radius=10,
        padding=15,
        content=Column(
            controls=[
                Container(
                    bgcolor=LIGHTBLUE,
                    border_radius=10,
                    padding=15,
                    content=Text(
                        "Balanço",
                        size=16,
                        weight="w700",
                        color=DEEPBLUE,
                    ),
                ),
                listaDeParticipantes,
            ]
        ),
    )

    layers_scroll = Row(height=280, scroll="auto")

    layers_scroll.controls.append(expenses_layer)
    layers_scroll.controls.append(balance_layer)

    expense_page = Container(
        width=400,
        height=850,
        bgcolor=DEEPBLUE,
        border_radius=20,
        padding=15,
        content=Column(
            controls=[
                Column(
                    [
                        Container(
                            Icon(icons.ARROW_BACK_IOS_NEW_ROUNDED, color=LIGHTBLUE),
                            margin=margin.only(left=15, right=10, top=30),
                            on_click=lambda _: page.go("/create_expense_page"),
                        ),
                        Container(
                            margin=margin.only(left=90, right=10, top=20, bottom=20),
                            content=Text(
                                "nome da despesa",  # buscar o nome da despesa no db e inserí-lo aqui
                                size=25,
                                color=LIGHTBLUE,
                                weight="w700",
                            ),
                        ),
                    ]
                ),
                layers_scroll,
                submit_button,
            ]
        ),
    )

    return expense_page
