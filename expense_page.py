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
        print("Partipantes", participants)
        
    submit_button = Container(
        content = Column(
            controls = [
                Stack(
                    controls = [
                        FloatingActionButton(
                            icon = icons.ADD, 
                            on_click = lambda e: on_submit(e),
                            bgcolor = LIGHTBLUE
                        )
                    ]
                )
            ]
        )
    )

    expenses_n_balance_layer = Container()

    add_expense = Container()

    expense_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,

        content = Column(
            controls = [
                submit_button
            ] 
        )
    )

    return (expense_page)