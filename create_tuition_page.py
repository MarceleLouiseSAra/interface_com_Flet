from flet import *
from custom_checkbox import CustomCheckBox

DEEPBLUE = '#432350'
MEDIUMBLUE = '#b476ff'
PINK = '#f4c9fd'
WHITE = '#ffffff'
LIGHTBLUE = '#B0C4DE'

page: Page

listaDeParticipantes = Column(
    height = 300,
    scroll = 'auto',
)

items = []
input_field = TextField(
    label = "Adicionar participante", 
    hint_text = "Insira aqui o nome do participante: ",
    border_color = MEDIUMBLUE,
    text_style = TextStyle(
        color = LIGHTBLUE
    ),
    autofocus = True,
    focused_border_color = PINK
)  # Campo de texto para inserir itens

def view_create_tuition_page(page: Page) -> Container:

    def addParticipante(e):
        item = input_field.value.strip()
        if item:  # Verifica se o item não está vazio
            items.append(item)  # Adiciona o item à lista
            input_field.value = ""  # Limpa o campo de texto
            listaDeParticipantes.controls.append( # Adiciona o item à exibição da lista
                Container(
                    margin = margin.only(left = 15, right = 10, top = 5),
                    width = 400,
                    height = 50,
                    bgcolor = LIGHTBLUE,
                    border_radius = 10,
                    padding = padding.only(
                        left = 20,
                        top = 15
                    ),
                    content = Text(item,
                                size = 15.5, 
                                color = DEEPBLUE, 
                                weight = 'w700'),
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
            on_click = addParticipante
        )
    )
    
    create_tuition_page = Container(
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
                        TextField(
                            label = "Nome da despesa",
                            hint_text = "Insira aqui o nome da despesa: ",
                            border_color = MEDIUMBLUE,
                            text_style = TextStyle(
                                color = MEDIUMBLUE
                            ),
                            focused_border_color = PINK
                        )
                    ]
                    )
                ),
                Container(
                    margin = margin.only(left = 15, right = 10, top = 15),
                    content = Column(
                        controls = [
                            input_field
                        ]
                    )
                ),
                add_button,
                listaDeParticipantes,
                Container(
                    height = 50,
                    width = 400,
                    margin = margin.only(left = 15, right = 10, top = 30),
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
                        on_click = lambda _: page.go('/')
                    )
                ),
            ]
        ),
    )

    return (create_tuition_page)