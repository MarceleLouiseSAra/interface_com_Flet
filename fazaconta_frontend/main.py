import flet as ft
from fazaconta_frontend.src.constants import Routes
from fazaconta_frontend.src.views.HomeView import HomeView
from fazaconta_frontend.src.views.LoginView import LoginView
from fazaconta_frontend.src.views.ViewNotFound import ViewNotFound

# from fazaconta_frontend.src.waiting_room_page import view_waiting_room_page

# from fazaconta_frontend.src.log_in_page import view_log_in_page
# from fazaconta_frontend.src.sign_in_page import view_sign_in_page
# from fazaconta_frontend.src.home_page import view_home_page
# from fazaconta_frontend.src.create_expense_page import view_create_expense_page
# from fazaconta_frontend.src.expense_page import view_expense_page
# from fazaconta_frontend.src.add_expense_page import view_add_expense_page


def main(page: ft.Page):
    page.title = "FazAConta"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.height = 900
    page.window.width = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # waiting_room_page = view_waiting_room_page(page)
    # log_in_page = view_log_in_page(page)
    # sign_in_page = view_sign_in_page(page)
    # home_page = view_home_page(page)
    # create_expense_page = view_create_expense_page(page)
    # expense_page = view_expense_page(page)
    # add_expense_page = view_add_expense_page(page)

    pages = {
        Routes.HOME: HomeView(page),
        Routes.LOGIN: LoginView(page),
        Routes.NOT_FOUND: ViewNotFound(page),
        # "/": ft.View(
        #     route="/waiting_room_page",
        #     controls=[waiting_room_page],
        #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #     vertical_alignment=ft.MainAxisAlignment.CENTER,
        # ),
        # "/log_in_page": ft.View(
        #     route="/log_in_page",
        #     controls=[log_in_page],
        #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #     vertical_alignment=ft.MainAxisAlignment.CENTER,
        # ),
        # "/sign_in_page": ft.View(
        #     route="/sign_in_page",
        #     controls=[sign_in_page],
        #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #     vertical_alignment=ft.MainAxisAlignment.CENTER,
        # ),
        # "/home_page": ft.View(
        #     route="/home_page",
        #     controls=[home_page],
        #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #     vertical_alignment=ft.MainAxisAlignment.CENTER,
        # ),
        # "/create_expense_page": ft.View(
        #     route="/create_expense_page",
        #     controls=[create_expense_page],
        #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #     vertical_alignment=ft.MainAxisAlignment.CENTER,
        # ),
        # "/expense_page": ft.View(
        #     route="/expense_page",
        #     controls=[expense_page],
        #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #     vertical_alignment=ft.MainAxisAlignment.CENTER,
        # ),
        # "/add_expense_page": ft.View(
        #     "/add_expense_page",
        #     [add_expense_page],
        #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #     vertical_alignment=ft.MainAxisAlignment.CENTER,
        # ),
    }

    def is_authenticated(page: ft.Page):
        return page.session.get("token") is not None

    def route_change(route):
        view = pages.get(Routes(page.route), ViewNotFound(page))
        if view.is_private and not is_authenticated(page):
            page.go(Routes.NOT_FOUND)
        else:
            page.views.clear()
            page.views.append(view)
            page.update()

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)