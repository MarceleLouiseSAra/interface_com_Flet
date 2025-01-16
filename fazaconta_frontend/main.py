import flet as ft
from fazaconta_frontend.src.constants import Routes
from fazaconta_frontend.src.utils import is_authenticated
from fazaconta_frontend.src.views.AddTransactionView import AddTransactionView
from fazaconta_frontend.src.views.CreateGroupView import CreateGroupView
from fazaconta_frontend.src.views.GroupDetailsView import GroupDetailsView
from fazaconta_frontend.src.views.GroupsListView import GroupsListView
from fazaconta_frontend.src.views.RegisterView import RegisterView
from fazaconta_frontend.src.views.HomeView import HomeView
from fazaconta_frontend.src.views.LoginView import LoginView
from fazaconta_frontend.src.views.ViewNotFound import ViewNotFound


def main(page: ft.Page):
    page.title = "FazAConta"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.height = 900
    page.window.width = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def route_change(route):
        page.views.clear()

        troute = ft.TemplateRoute(page.route)

        if troute.match(Routes.HOME):
            view = HomeView(page)
        elif troute.match(Routes.LOGIN):
            view = LoginView(page)
        elif troute.match(Routes.REGISTER):
            view = RegisterView(page)
        elif troute.match(Routes.CREATE_GROUP):
            view = CreateGroupView(page, is_private=True)
        elif troute.match(Routes.GROUPS_LIST):
            view = GroupsListView(page, is_private=True)
        elif troute.match(Routes.GROUP_DETAILS):
            group_id = troute.id
            view = GroupDetailsView(page, group_id, is_private=True)
        elif troute.match(Routes.CREATE_TRANSACTION):
            group_id = troute.group_id
            view = AddTransactionView(page, group_id, is_private=True)
        elif troute.match(Routes.NOT_FOUND):
            view = ViewNotFound(page)
        else:
            if is_authenticated(page):
                view = GroupsListView(page, is_private=True)
            else:
                view = ViewNotFound(page)

        if (
            hasattr(view, "is_private")
            and view.is_private
            and not is_authenticated(page)
        ):
            view = LoginView(page)

        page.views.append(view)
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)
