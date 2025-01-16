from datetime import datetime
import flet as ft
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


def is_authenticated(page: ft.Page):
    return page.client_storage.get("token") is not None


def to_money(amount: float):
    return locale.currency(amount, grouping=True)


def to_formatted_date(date: datetime):

    return date.strftime("%d de %B de %Y")
