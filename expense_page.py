from flet import *
from custom_checkbox import CustomCheckBox

DEEPBLUE = '#432350'
MEDIUMBLUE = '#b476ff'
PINK = '#f4c9fd'
WHITE = '#ffffff'
LIGHTBLUE = '#B0C4DE'

page: Page

participants = ['joão', 'marcele'] # puxar do db

def view_expense_page(page: Page) -> Container:
        
    submit_button = Container(
        content = Column(
            controls = [
                Stack(
                    controls = [
                        FloatingActionButton(
                            top = 300,
                            left = 150,
                            icon = icons.ADD, 
                            on_click = lambda _: page.go('/add_expense_page'),
                            bgcolor = LIGHTBLUE
                        )
                    ]
                )
            ]
        )
    )

    expenses_layer = Container(
        width = 350,
        height = 300,
        bgcolor = MEDIUMBLUE,
        border_radius = 10,
        padding = 15,

        content = Column(
            controls = [
                Container(
                    width = 350,
                    bgcolor = LIGHTBLUE,
                    border_radius = 10,
                    padding = 15,

                    content = Text(
                        "Total gasto",
                        size = 16,
                        weight = 'w700',
                        color = DEEPBLUE,
                    ),
                ),
                Row([
                    Container(
                        margin = margin.only(left = 105, right = 10, top = 10),

                        content = Row(
                            controls = [
                                Text(
                                    "R$",
                                    size = 20,
                                    color = WHITE,
                                    weight = 'w700'
                                ),
                                Text(
                                    "100,00", # puxar do db
                                    size = 20,
                                    color = WHITE,
                                    weight = 'w700'
                                ),
                            ],
                            alignment = MainAxisAlignment.START
                        ),
                    ),
                ]),
            ],
            horizontal_alignment = CrossAxisAlignment.CENTER
        )
    )

    listaDeParticipantes = Column(
        scroll = 'auto',
    )

    for participant in participants:
        listaDeParticipantes.controls.append(
            Container(
                margin = margin.only(left = 15, right = 10, top = 5),
                width = 320,
                height = 70,
                bgcolor = LIGHTBLUE,
                border_radius = 10,
                padding = padding.only(
                    left = 20,
                    top = 20
                ),
                content = CustomCheckBox(color = PINK, # arrumar a CustomBox (mudar a cor e, toda vez que clicarmos, o participante seja retirado)
                                        label_color = DEEPBLUE, 
                                        label = participant,
                                        size = 30,
                                        font_size = 15),
            )
        )

    balance_layer = Container(
        width = 350,
        height = 300,
        bgcolor = MEDIUMBLUE,
        border_radius = 10,
        padding = padding.only(
            top = 10,
            bottom = 10
        ),

        content = listaDeParticipantes
    )

    layers_scroll = Row(
        height = 280,
        scroll = 'auto'
    )

    layers_scroll.controls.append(expenses_layer)
    layers_scroll.controls.append(balance_layer)

    expense_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,
        padding = 15,

        content = Column(
            controls = [
                Column([
                    Container(
                        Icon(icons.ARROW_BACK_IOS_NEW_ROUNDED, color = LIGHTBLUE),
                        margin = margin.only(left = 15, right = 10, top = 30),
                        on_click = lambda _: page.go('/create_expense_page'),
                    ),
                    Container(
                        margin = margin.only(left = 90, right = 10, top = 20),
                        content = Text(
                            "nome da despesa", # buscar o nome da despesa no db e inserí-lo aqui
                            size = 25,
                            color = LIGHTBLUE,
                            weight = 'w700'
                        )
                    ),
                ]),
                layers_scroll,
                submit_button,
            ] 
        )
    )

    return (expense_page)