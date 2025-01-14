from flet import *
from .custom_checkbox import CustomCheckBox
import requests


DEEPBLUE = "#432350"
MEDIUMBLUE = "#b476ff"
PINK = "#f4c9fd"
WHITE = "#ffffff"
LIGHTBLUE = "#B0C4DE"

page: Page

expenses = ["viagem", "restaurante", "compras de fim de ano"]  # puxar do db


def view_home_page(page: Page) -> Container:

    def shrink(e):
        side_bar.controls[0].width = 200
        side_bar.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right
        )
        side_bar.controls[0].border_radius = border_radius.only(
            top_left=20, top_right=0, bottom_left=20, bottom_right=0
        )
        side_bar.update()

    def restore(e):
        side_bar.controls[0].width = 400
        side_bar.controls[0].border_radius = 20
        side_bar.controls[0].scale = transform.Scale(
            1, alignment=alignment.center_right
        )
        side_bar.update()

    circle = Stack(
        controls=[
            Container(width=100, height=100, border_radius=50, bgcolor=LIGHTBLUE),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=["#00000000", PINK],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(
                    alignment="center",
                    controls=[
                        Container(
                            padding=padding.all(5),
                            bgcolor=DEEPBLUE,
                            width=90,
                            height=90,
                            border_radius=50,
                            content=Container(
                                bgcolor=MEDIUMBLUE,
                                height=80,
                                width=80,
                                border_radius=40,
                                content=CircleAvatar(
                                    opacity=0.8,
                                    foreground_image_url="https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8MEDIUMBLUEVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
                                    # puxar do db
                                ),
                            ),
                        )
                    ],
                ),
            ),
        ]
    )

    outgoings = Column(height=435, scroll="auto")

    for expense in expenses:  # puxar os dados de quantas desespesas têm-se da db
        outgoings.controls.append(
            Container(
                height=70,
                width=400,
                bgcolor=DEEPBLUE,
                border_radius=10,
                padding=padding.only(left=20, top=20),
                content=CustomCheckBox(
                    color=PINK, label_color=WHITE, label=expense, size=30, font_size=15
                ),
            )
        )

    groups_card = Row(scroll="auto")

    groups = ["Trabalho", "Família", "Amigos"]  # puxar do db

    for group in groups:
        groups_card.controls.append(
            Container(
                width=150,
                height=90,
                border_radius=10,
                bgcolor=DEEPBLUE,
                padding=15,
                content=Column(
                    controls=[
                        Text(group, color=WHITE),
                        Container(
                            width=160,
                            height=5,
                            bgcolor=LIGHTBLUE,
                            border_radius=20,
                            padding=padding.only(
                                right=80
                            ),  # se mudar o padding, a barrinha  cresce
                            content=Container(bgcolor=PINK),
                        ),
                    ],
                    alignment="spaceBetween",
                ),
            )
        )

    main_page = Container(
        content=Column(
            controls=[
                Row(
                    alignment="spaceBetween",
                    controls=[
                        Container(
                            on_click=lambda e: shrink(e),
                            # on_click = request_data,
                            content=Icon(icons.MENU, color=WHITE),
                        ),
                        Row(
                            controls=[
                                Container(
                                    Icon(icons.SEARCH, color=WHITE),
                                    #
                                ),
                                Container(
                                    Icon(icons.NOTIFICATIONS_OUTLINED, color=WHITE),
                                    on_click=lambda _: page.go("/"),
                                ),
                            ]
                        ),
                    ],
                ),
                Text(
                    value="Olá, João!", size=28, weight="bold", color=WHITE
                ),  # puxar do db
                Text(value="GRUPOS", weight="bold", color=WHITE),
                Container(content=groups_card),
                Container(padding=padding.all(15)),
                Text(value="COBRANÇAS PENDENTES", weight="bold", color=WHITE),
                Stack(
                    controls=[
                        outgoings,
                        FloatingActionButton(
                            bottom=2,
                            right=20,
                            icon=icons.ADD,
                            on_click=lambda _: page.go("/create_expense_page"),
                            # on_click = lambda e: alertDialog(page),
                            bgcolor=LIGHTBLUE,
                        ),
                    ]
                ),
            ]
        )
    )

    side_bar = Row(
        alignment="end",
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=MEDIUMBLUE,
                border_radius=20,
                animate=animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve="decelerate"),
                padding=padding.only(top=50, left=20, right=20, bottom=5),
                content=Column(controls=[main_page]),
            )
        ],
    )

    info_content_page = Container(
        width=400,
        height=850,
        bgcolor=DEEPBLUE,
        border_radius=35,
        padding=padding.only(left=50, top=60, right=200),
        content=Column(
            controls=[
                Container(
                    animate=animation.Animation(600, AnimationCurve.DECELERATE),
                    animate_scale=animation.Animation(400, curve="decelerate"),
                ),
                Stack(
                    controls=[
                        FloatingActionButton(
                            icon=icons.HOME,
                            on_click=lambda e: restore(e),
                            bgcolor=LIGHTBLUE,
                        ),
                    ]
                ),
                Container(
                    height=20,
                ),
                circle,
                Text(
                    "João\nPirajá", size=32, weight="bold", color=LIGHTBLUE
                ),  # puxar do db
                Container(height=5),
                Container(
                    content=Column(
                        controls=[
                            Row(
                                controls=[
                                    Container(
                                        on_click=lambda _: page.go("/"),
                                        content=Icon(
                                            icons.ACCOUNT_CIRCLE_ROUNDED,
                                            color=LIGHTBLUE,
                                        ),
                                    ),
                                    Text(
                                        "Minha conta",
                                        color=LIGHTBLUE,
                                        weight=FontWeight.W_300,
                                        font_family="poppins",
                                    ),
                                ]
                            ),
                            Row(
                                controls=[
                                    Container(
                                        on_click=lambda _: page.go("/"),
                                        content=Icon(
                                            icons.ADMIN_PANEL_SETTINGS_ROUNDED,
                                            color=LIGHTBLUE,
                                        ),
                                    ),
                                    Text(
                                        "Configurações",
                                        color=LIGHTBLUE,
                                        weight=FontWeight.W_300,
                                        font_family="poppins",
                                    ),
                                ]
                            ),
                            Row(
                                controls=[
                                    Container(
                                        on_click=lambda _: page.go("/"),
                                        content=Icon(
                                            icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                            color=LIGHTBLUE,
                                        ),
                                    ),
                                    Text(
                                        "Sair",
                                        color=LIGHTBLUE,
                                        weight=FontWeight.W_300,
                                        font_family="poppins",
                                    ),
                                ]
                            ),
                        ]
                    )
                ),
            ]
        ),
    )

    home_page = Container(
        width=400,
        height=850,
        bgcolor=DEEPBLUE,
        border_radius=20,
        content=Stack(controls=[info_content_page, side_bar]),
    )

    return home_page
