from flet import *
from waiting_room_page import view_waiting_room_page
from log_in_page import view_log_in_page
from sign_in_page import view_sign_in_page
from home_page import view_home_page
from create_expense_page import view_create_expense_page
from expense_page import view_expense_page

def main(page: Page):

    page.title = "fazAConta"
    page.theme_mode = 'dark'

    waiting_room_page = view_waiting_room_page(page)
    log_in_page = view_log_in_page(page)
    sign_in_page = view_sign_in_page(page)
    home_page = view_home_page(page)
    create_expense_page = view_create_expense_page(page)
    expense_page = view_expense_page(page)

    pages = {
        '/': View("/waiting_room_page", [waiting_room_page]),
        '/log_in_page': View("/log_in_page", [log_in_page]),
        '/sign_in_page': View("/sign_in_page", [sign_in_page]),
        '/home_page': View("/home_page", [home_page]),
        '/create_expense_page': View("/create_expense_page", [create_expense_page]),
        '/expense_page': View("/expense_page", [expense_page]),
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

app(target = main)