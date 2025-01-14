import flet as ft


# Base view class
class View:
    def __init__(self, route: str, is_private: bool = False):
        self.route = route
        self.is_private = is_private

    def build(self, page):
        raise NotImplementedError(
            "The 'build' method must be implemented in the subclass."
        )


# Home view class
class HomeView(View):
    def __init__(self):
        super().__init__("/", is_private=False)

    def build(self, page):
        return ft.Column(
            [
                ft.Text("Welcome to the Home Page", size=24, weight="bold"),
                ft.ElevatedButton(
                    "Go to About Page", on_click=lambda e: page.go("/about")
                ),
                ft.ElevatedButton(
                    "Go to Private Page", on_click=lambda e: page.go("/private")
                ),
            ]
        )


# About view class
class AboutView(View):
    def __init__(self):
        super().__init__("/about", is_private=False)

    def build(self, page):
        return ft.Column(
            [
                ft.Text("About Page", size=24, weight="bold"),
                ft.ElevatedButton("Back to Home", on_click=lambda e: page.go("/")),
            ]
        )


# Private view class
class PrivateView(View):
    def __init__(self):
        super().__init__("/private", is_private=True)

    def build(self, page):
        return ft.Column(
            [
                ft.Text("Private Page - Welcome!", size=24, weight="bold"),
                ft.ElevatedButton("Back to Home", on_click=lambda e: page.go("/")),
            ]
        )


# Login view class
class LoginView(View):
    def __init__(self):
        super().__init__("/login", is_private=False)

    def build(self, page):
        return ft.Column(
            [
                ft.Text(
                    "Please log in to access private pages.", size=24, weight="bold"
                ),
                ft.ElevatedButton("Log in", on_click=lambda e: self.log_in(page)),
            ]
        )

    def log_in(self, page):
        page.session.set("is_authenticated", True)
        page.go("/private")


# Main app class
class MyApp:
    def __init__(self):
        self.routes = {
            "/": HomeView(),
            "/about": AboutView(),
            "/private": PrivateView(),
            "/login": LoginView(),
        }

    def is_authenticated(self, page):
        return page.session.get("is_authenticated", False)

    def main(self, page: ft.Page):
        page.title = "Flet App with Private Routes"
        page.update()

        def on_route_change(route):
            view = self.routes.get(route, None)
            if view is None:
                # Handle 404
                page.views.clear()
                page.views.append(
                    ft.View(
                        route=route,
                        controls=[
                            ft.Text("404 - Page Not Found", size=24, weight="bold"),
                            ft.ElevatedButton(
                                "Go to Home", on_click=lambda e: page.go("/")
                            ),
                        ],
                    )
                )
            elif view.is_private and not self.is_authenticated(page):
                # Redirect to login if not authenticated
                page.go("/login")
            else:
                # Load the requested view
                page.views.clear()
                page.views.append(ft.View(route=route, controls=[view.build(page)]))

            page.update()

        page.on_route_change = on_route_change
        page.go("/")


# Run the app
if __name__ == "__main__":
    app = MyApp()
    ft.app(target=app.main)
