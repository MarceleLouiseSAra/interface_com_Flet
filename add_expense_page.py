from flet import *
from create_expense_page import participants

DEEPBLUE = '#432350'
MEDIUMBLUE = '#b476ff'
PINK = '#f4c9fd'
WHITE = '#ffffff'
LIGHTBLUE = '#B0C4DE'

page: Page

def view_add_expense_page(page: Page) -> Container:

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
                ]),
            ]
        )
    )

    return (add_expense_page)