from flet import *
from custom_checkbox import CustomCheckBox

DEEPBLUE = '#432350'
MEDIUMBLUE = '#b476ff'
PINK = '#f4c9fd'
WHITE = '#ffffff'
LIGHTBLUE = '#B0C4DE'

page: Page

participants = []

def view_create_expense_page(page: Page) -> Container:

    listaDeParticipantes = Column(
        height = 300,
        scroll = 'auto',
    )

    partipant_input = TextField(
        label = "Adicionar participante", 
        hint_text = "Insira aqui o nome do participante: ",
        border_color = MEDIUMBLUE,
        text_style = TextStyle(
            color = LIGHTBLUE
        ),
        autofocus = True,
        focused_border_color = PINK
    )  # Campo de texto para inserir partipantes

    def addParticipante(e):

        item = partipant_input.value.strip()
        if item:  # Verifica se o item não está vazio
            participants.append(item)  # Adiciona o item à lista
            partipant_input.value = ""  # Limpa o campo de texto
            listaDeParticipantes.controls.append( # Adiciona o item à exibição da lista
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
                                            label = item,
                                            size = 30,
                                            font_size = 15),
                )
            )  # Adiciona o item à exibição da lista
            page.update()  # Atualiza a página para refletir as mudanças

    # Botão para adicionar o item
    add_button = Container(
        margin = margin.only(left = 15, right = 10, top = 15),
        content = TextButton(
            "Adicionar participante",
            style = ButtonStyle(
                color = {
                    ControlState.HOVERED: LIGHTBLUE,
                    ControlState.FOCUSED: WHITE,
                    ControlState.DEFAULT: PINK,
                },
                bgcolor = MEDIUMBLUE
            ),
            on_click = lambda e: addParticipante(e)
        )
    )

    expense_input = TextField(
        label = "Nome da despesa",
        hint_text = "Insira aqui o nome da despesa: ",
        border_color = MEDIUMBLUE,
        text_style = TextStyle(
            color = LIGHTBLUE
        ),
        autofocus = True,
        focused_border_color = PINK
    )  # Campo de texto para inserir o nome da despesa

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
                            on_click = lambda _: page.go('/expense_page')
                        )
                    )
        
    create_expense_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,
        padding = padding.only(left = 30, top = 30, right = 30),

        content = Column(
            controls = [
                Row([
                    Container(
                        Icon(icons.ARROW_BACK_IOS_NEW_ROUNDED, color = LIGHTBLUE),
                        margin = margin.only(left = 15, right = 10, top = 30),
                        on_click = lambda _: page.go('/home_page'),
                    ),
                    Container(
                        margin = margin.only(left = 30, right = 10, top = 30),
                        content = Text(
                            "Criar despesa",
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
                            expense_input
                        ]
                    )
                ),
                Container(
                    margin = margin.only(left = 15, right = 10, top = 15),
                    content = Column(
                        controls = [
                            partipant_input
                        ]
                    )
                ),
                add_button,
                listaDeParticipantes,
                submit_button,
            ]
        ),
    )

    return (create_expense_page)