from flet import *
from create_expense_page import participants
from custom_checkbox import CustomCheckBox

DEEPBLUE = '#432350'
MEDIUMBLUE = '#b476ff'
PINK = '#f4c9fd'
WHITE = '#ffffff'
LIGHTBLUE = '#B0C4DE'

page: Page

participants = ['joão', 'marcele', 'caio', 'maria'] # puxar do db
devedores = ['joão', 'marcele', 'caio', 'maria'] # puxar do db

def view_add_expense_page(page: Page) -> Container:

    title_input = TextField(
        label = "Adicionar nome", 
        hint_text = "Insira aqui o nome desta despesa: ",
        border_color = MEDIUMBLUE,
        text_style = TextStyle(
            color = LIGHTBLUE
        ),
        autofocus = True,
        focused_border_color = PINK
    )  # Campo de texto para inserir partipantes

    amount_input = TextField(
        label = "Adicionar custo",
        hint_text = "Insira aqui o custo desta despesa: ",
        border_color = MEDIUMBLUE,
        text_style = TextStyle(
            color = LIGHTBLUE
        ),
        autofocus = True,
        focused_border_color = PINK
    )  # Campo de texto para inserir o nome da despesa

    radio = RadioGroup(
        content = Column([
            Radio(value=opcao, label=opcao) for opcao in participants
        ])
    )

    listaDeParticipantes = Column(
        height = 100,
        scroll = 'auto',
    )

    listaDeParticipantes.controls.append(radio) # retorna o resultado de radio e retirar da listaDeDevedores quem pagou pela despesa

    listaDeDevedores = Column(
        height = 200,
        scroll = 'auto',
    )

    for devedor in devedores:
        listaDeDevedores.controls.append( # Adiciona o item à exibição da lista
            Container(
                margin = margin.only(left = 15, right = 10, top = 5),
                width = 400,
                height = 70,
                bgcolor = LIGHTBLUE,
                border_radius = 10,
                padding = padding.only(
                    left = 20,
                top = 20
                ),
                content = CustomCheckBox(color = PINK, # arrumar a CustomBox (mudar a cor e, toda vez que clicarmos, o participante seja retirado)
                                        label_color = DEEPBLUE, 
                                        label = devedor,
                                        size = 30,
                                        font_size = 15),
            )
        )

    def on_submit(e): # análogo ao request_data
        page.go('/expense_page')
        #criar popup

    submit_button = Container(
                    margin = margin.only(left = 115, right = 0, top = 30),
                    content = TextButton(
                        "Criar despesa",
                        style = ButtonStyle(
                            color = {
                                ControlState.HOVERED: LIGHTBLUE,
                                ControlState.FOCUSED: WHITE,
                                ControlState.DEFAULT: PINK,
                            },
                            bgcolor = MEDIUMBLUE,
                        ),
                        on_click = lambda e: on_submit(e) # substituir pelo request_data
                    )
                )

    add_expense_page = Container(
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
                        margin = margin.only(left = 70, right = 10, top = 30),
                        content = Text(
                            "Adicionar despesa",
                            size = 28,
                            color = LIGHTBLUE,
                            weight = 'w700'
                        )
                    ),
                ]),
                Container(
                    margin = margin.only(left = 15, right = 10, top = 15),
                    content = Column(
                        controls = [
                            title_input
                        ]
                    )
                ),
                Container(
                    margin = margin.only(left = 15, right = 10, top = 15),
                    content = Column(
                        controls = [
                            amount_input
                        ]
                    )
                ),
                Row([
                    Container(
                        margin = margin.only(left = 15, right = 10, top = 15),
                        content = Column(
                            controls = [
                                Text(
                                    "Pago por: ",
                                    size = 16,
                                    color = LIGHTBLUE,
                                    weight = 'w700'
                                ),
                                listaDeParticipantes
                            ]
                        )
                    ),
                    Container(
                        margin = margin.only(left = 15, right = 10, top = 15),
                        content = Column(
                            controls = [
                                Text(
                                    "Pago em: ",
                                    size = 16,
                                    color = LIGHTBLUE,
                                    weight = 'w700'
                                ),
                            ]
                        )
                    )
                ]),
                Container(
                    margin = margin.only(left = 15, right = 10, top = 30),
                    content = Column(
                        controls = [
                            Text(
                                "Participantes da partilha: ",
                                size = 16,
                                color = LIGHTBLUE,
                                weight = 'w700'
                            ),
                            listaDeDevedores
                        ],
                    )
                ),
                submit_button,
            ]
        )
    )

    return (add_expense_page)