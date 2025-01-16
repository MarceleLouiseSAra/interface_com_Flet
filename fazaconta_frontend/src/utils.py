import flet as ft


def is_authenticated(page: ft.Page):
    return page.client_storage.get("token") is not None
