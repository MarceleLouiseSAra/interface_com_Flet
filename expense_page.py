from flet import *
from create_expense_page import participants

DEEPBLUE = '#432350'
MEDIUMBLUE = '#b476ff'
PINK = '#f4c9fd'
WHITE = '#ffffff'
LIGHTBLUE = '#B0C4DE'

page: Page

def view_expense_page(page: Page) -> Container:

    def on_submit(e):
        print("Partipantes:", participants)
        
    submit_button = Container(
        content = Column(
            controls = [
                Stack(
                    controls = [
                        FloatingActionButton(
                            top = 100,
                            left = 170,
                            icon = icons.ADD, 
                            on_click = lambda e: on_submit(e),
                            bgcolor = LIGHTBLUE
                        )
                    ]
                )
            ]
        )
    )

    expenses_layer = Container(
        width = 100,
        height = 100,
        bgcolor = WHITE,
        border_radius = 20,
    )

    balance_layer = Container(
        width = 100,
        height = 100,
        bgcolor = MEDIUMBLUE,
        border_radius = 20,
    )

    expense_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,

        content = Column(
            controls = [
                Row([
                    Container(
                        Icon(icons.ARROW_BACK_IOS_NEW_ROUNDED, color = LIGHTBLUE),
                        margin = margin.only(left = 15, right = 10, top = 30),
                        on_click = lambda _: page.go('/create_expense_page'),
                    ),
                    Container(
                        margin = margin.only(left = 30, right = 10, top = 30),
                        content = Text(
                            "nome da despesa",
                            size = 28,
                            color = LIGHTBLUE,
                            weight = 'w700'
                        )
                    ),
                ]),
                Row([
                    expenses_layer,
                    balance_layer,
                ]),
                Container(),
                submit_button,
            ] 
        )
    )

    return (expense_page)