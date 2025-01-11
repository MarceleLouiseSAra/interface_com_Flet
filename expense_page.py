from flet import *
from custom_checkbox import CustomCheckBox

DEEPBLUE = '#432350'
MEDIUMBLUE = '#b476ff'
PINK = '#f4c9fd'
WHITE = '#ffffff'
LIGHTBLUE = '#B0C4DE'

page: Page

def view_expense_page(page: Page) -> Container:

    def shrink(e):
            add_expense.controls[0].width = 200
            add_expense.controls[0].scale = transform.Scale(
                0.8,
                alignment = alignment.center_right
            )
            add_expense.controls[0].border_radius = border_radius.only(
                top_left = 20,
                top_right = 0,
                bottom_left = 20,
                bottom_right = 0
            )
            add_expense.update()

    def restore(e):
        add_expense.controls[0].width = 400
        add_expense.controls[0].border_radius = 20
        add_expense.controls[0].scale = transform.Scale(
            1,
            alignment = alignment.center_right
        )
        add_expense.update()

    expenses_n_balance_layer = Container()

    add_expense = Container()

    expense_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,

        content = Stack(
            controls = [
                expenses_n_balance_layer,
                add_expense,
            ]
        )
    )

    return (expense_page)