from flet import *

DEEPBLUE = '#432350'
MEDIUMBLUE = '#b476ff'
PINK = '#f4c9fd'
WHITE = '#ffffff'
LIGHTBLUE = '#B0C4DE'

page: Page

def view_create_tuition_page(page: Page) -> Container:

    create_tuition_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,
        padding = padding.only(left = 30, top = 30, right = 30),

        content = Column(
            controls = [
                Stack(
                    controls = [
                        FloatingActionButton(
                            icon = icons.HOME, 
                            on_click = lambda _: page.go('/home_page'),
                            bgcolor = LIGHTBLUE
                        )
                    ],
                ),
                Container(
                    alignment = alignment.center,
                    padding = padding.only(top = 30),
                    content = Text(
                        "Criar despesa",
                        size = 30,
                        color = LIGHTBLUE,
                        weight = 'w700'
                    )
                ),
                Container(
                    alignment = alignment.center,
                    padding = padding.only(top = 15),
                    content = Text(
                        "Por favor, preencha as informações a seguir:",
                        size = 16,
                        color = LIGHTBLUE,
                        text_align = "center"
                    )
                ),
                Container(
                    padding = padding.only(top = 10),
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
                    padding = padding.only(top = 10),
                    content = Column(
                        controls = [
                            TextField(
                                label = "Valor da despesa",
                                hint_text = "Quanto esta despesa custou?: ",
                                border_color = MEDIUMBLUE,
                                text_style = TextStyle(
                                    color = MEDIUMBLUE
                                ),
                                focused_border_color = PINK
                            )
                        ]
                    )
                ),
                # Container(
                #     padding = padding.only(top = 10),
                #     content = Column(
                #         controls=[
                #             Text("Grupo da despesa:", size = 16),
                #             TextButton(
                #                 content = Text(value = groups[2], ref = selected_group_ref, size = 16),
                #                 style = ButtonStyle(color = MEDIUMBLUE),
                #                 on_click = lambda e: page.open(
                #                     CupertinoBottomSheet(
                #                         cupertino_picker,
                #                         height = 216,
                #                         padding = padding.only(top=6),
                #                     )
                #                 ),
                #             ),
                #         ],
                #     )
                # ),
                Container(
                    padding = padding.only(top = 10),
                    content = Column(
                        controls = [
                            TextField(
                                label = "Senha",
                                hint_text = "Insira a sua senha aqui: ",
                                password = True,
                                can_reveal_password = True,
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
                    alignment = alignment.center,
                    padding = padding.only(top = 10),
                    content = TextButton(
                        "Criar despesa",
                        style = ButtonStyle(
                            color = {
                                ControlState.HOVERED: LIGHTBLUE,
                                ControlState.FOCUSED: WHITE,
                                ControlState.DEFAULT: PINK,
                            },
                            bgcolor = MEDIUMBLUE
                        ),
                        # on_click = lambda e: inserirDados(e)
                    )
                )
            ]
        )
    )

    return (create_tuition_page)