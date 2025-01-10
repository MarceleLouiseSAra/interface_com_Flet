from flet import *

DEEPBLUE = '#432350'
MEDIUMBLUE = '#b476ff'
PINK = '#f4c9fd'
WHITE = '#ffffff'
LIGHTBLUE = '#B0C4DE'

page: Page

def view_waiting_room_page(page: Page) -> Container:

    waiting_room_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,
        margin = 10,
        padding = 10,
        alignment = alignment.center,

        content = Column(
            controls = [
                Column([
                    Container(
                        content = Text(
                            value = "fazAConta", 
                            size = 28, 
                            weight = 'bold', 
                            color = LIGHTBLUE
                        ),
                        margin = margin.only(top = 100, left = 35)
                    ),
                    Row([
                        Container(
                            width = 150,
                            content = TextButton(
                                "Criar conta",
                                style = ButtonStyle(
                                    bgcolor = MEDIUMBLUE,
                                    color = {
                                        ControlState.HOVERED: WHITE,
                                        ControlState.FOCUSED: MEDIUMBLUE,
                                        ControlState.DEFAULT: DEEPBLUE,
                                    }
                                ),
                                on_click = lambda _: page.go('/sign_in_page'),
                            ),
                            margin = margin.only(top = 400, left = 35)
                        ),
                        Container(
                            width = 150,
                            content = TextButton(
                                "Entrar",
                                style = ButtonStyle(
                                    bgcolor = MEDIUMBLUE,
                                    color = {
                                        ControlState.HOVERED: WHITE,
                                        ControlState.FOCUSED: MEDIUMBLUE,
                                        ControlState.DEFAULT: DEEPBLUE,
                                    }
                                ),
                                on_click = lambda _: page.go('/log_in_page'),
                            ),
                            margin = margin.only(top = 400, left = 5)
                        )
                    ])
                ])
            ],
        )
    )
    
    return (waiting_room_page)