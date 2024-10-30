from flet import *
from custom_checkbox import CustomCheckBox

def main(page = Page):
    
    page.title = "aplicativo muito massa"

    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    WHITE = '#ffffff'
    LIGHTSTEELBLUE = '#B0C4DE'

    def shrink(e):
        page_2.controls[0].width = 200
        page_2.controls[0].scale = transform.Scale(
            0.8,
            alignment = alignment.center_right
        )
        page_2.controls[0].border_radius = border_radius.only(
            top_left = 20,
            top_right = 0,
            bottom_left = 20,
            bottom_right = 0
        )
        page_2.update()

    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].border_radius = 20
        page_2.controls[0].scale = transform.Scale(
            1,
            alignment = alignment.center_right
        )
        page_2.update()

    circle = Stack(
        controls = [
            Container(
                width = 100,
                height = 100,
                border_radius = 50,
                bgcolor = LIGHTSTEELBLUE
            ),
            Container(
                gradient = SweepGradient(
                    center = alignment.center,
                    start_angle = 0.0,
                    end_angle = 3,
                    stops = [0.5, 0.5],
                    colors = ['#00000000', PINK]
                ),
                width = 100,
                height = 100,
                border_radius = 50,
                content = Row(
                    alignment = 'center',
                    controls = [
                        Container(
                            padding = padding.all(5),
                            bgcolor = BG,
                            width = 90,
                            height = 90,
                            border_radius = 50,
                            content = Container(
                                bgcolor = FG,
                                height = 80,
                                width = 80,
                                border_radius = 40,
                                content = CircleAvatar(
                                    opacity = 0.8,
                                    foreground_image_url = "https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
                                )
                            )
                        )
                    ]
                )
            )
        ]
    )

    outgoings = Column(
        height = 435,
        scroll = 'auto'
    )

    for i in range(10): # puxar os dados de quantas desespesas têm-se da db
        outgoings.controls.append(
            Container(
                height = 70,
                width = 400,
                bgcolor = BG,
                border_radius = 10,
                padding = padding.only(
                    left = 20,
                    top = 20
                ),
                content = CustomCheckBox(color = PINK, 
                                         label_color = WHITE, 
                                         label = 'turn coffee into code',
                                         size = 30,
                                         font_size = 15)
            )
        )

    groups_card = Row(
        scroll = 'auto'
    )

    groups = ['Trabalho', 'Família', 'Amigos'] # fazer disso um dicionário?, importar da db?

    for group in groups:
        groups_card.controls.append(
            Container(
                width = 150,
                height = 90,
                border_radius = 10,
                bgcolor = BG,
                padding = 15,

                content = Column(
                    controls = [
                        Text(group, color = WHITE),
                        Container( # espaço entre os objetos
                            padding = padding.only(
                                top = 10,
                                bottom = 10
                            )
                        ),
                        Container(
                            width = 160,
                            height = 5,
                            bgcolor = LIGHTSTEELBLUE,
                            border_radius = 20,
                            padding = padding.only(right = 80), # se mudar o padding, a barrinha  cresce

                            content = Container(
                                bgcolor = PINK
                            )

                        )
                    ]
                )
            )
        )

    login_page = Container()

    sign_in_page = Container()

    first_page_contents = Container(
        content = Column(
            controls = [
                Row(
                    alignment = 'spaceBetween',
                    controls = [
                        Container(
                            on_click = lambda e: shrink(e),
                            content = Icon(icons.MENU, color = WHITE)
                        ),
                        Row(
                            controls = [
                                Icon(icons.SEARCH, color = WHITE),
                                Icon(icons.NOTIFICATIONS_OUTLINED, color = WHITE)
                            ]
                        )
                    ]
                ),
                Text(value = "Olá, João!", size = 28, weight = 'bold', color = WHITE),
                Text(value = 'GRUPOS', weight = 'bold', color = WHITE),
                Container(
                    content = groups_card
                ),
                Container(
                    padding = padding.all(15)
                ),
                Text(value = 'COBRANÇAS PENDENTES', weight = 'bold', color = WHITE),
                Stack(
                    controls = [
                        outgoings,
                        FloatingActionButton(
                            bottom = 2,
                            right = 20,
                            icon = icons.ADD, 
                            on_click = lambda _: page.go('/create_tuition'),
                            bgcolor = LIGHTSTEELBLUE
                        )
                    ]
                )
            ]
        )
    )

    page_1 = Container(
        width = 400,
        height = 850,
        bgcolor = BG,
        border_radius = 35,
        padding = padding.only(
            left = 50,
            top = 60,
            right = 200
        ),
        content = Column(
            controls = [
                Container(
                    animate = animation.Animation(600, AnimationCurve.DECELERATE),
                    animate_scale = animation.Animation(400, curve = 'decelerate')
                ),
                Stack(
                    controls = [
                        FloatingActionButton(
                            icon = icons.HOME, 
                            on_click = lambda e: restore(e),
                            bgcolor = LIGHTSTEELBLUE
                        ),
                    ]
                ),
                Container(
                    height = 20,
                ),
                circle,
                Text('João\nPirajá', size = 32, weight = 'bold', color = LIGHTSTEELBLUE),
                Container(
                    height = 2
                ),
                Row(
                    controls = [
                        Icon(icons.ACCOUNT_CIRCLE_ROUNDED, color = LIGHTSTEELBLUE),
                        Text(
                            'Minha conta',
                            color = LIGHTSTEELBLUE,
                            weight = FontWeight.W_300,
                            font_family = 'poppins'
                        )
                    ]
                ),
                Container(
                    height = 2,
                ),
                Row(
                    controls = [
                        Icon(icons.FAVORITE_BORDER_ROUNDED, color = LIGHTSTEELBLUE),
                        Text(
                            'Templates',
                            color = LIGHTSTEELBLUE,
                            weight = FontWeight.W_300,
                            font_family = 'poppins'
                        )
                    ]
                ),
                Container(
                    height = 2,
                ),
                Row(
                    controls = [
                        Icon(icons.ADMIN_PANEL_SETTINGS_ROUNDED, color = LIGHTSTEELBLUE),
                        Text(
                            'Configurações',
                            color = LIGHTSTEELBLUE,
                            weight = FontWeight.W_300,
                            font_family = 'poppins'
                        )
                    ]
                ) # to-do: fazer dessas abas clicáveis
            ]
        )
    )

    page_2 = Row(
        alignment = 'end',
        controls = [
            Container(
                width = 400,
                height = 850,
                bgcolor = FG,
                border_radius = 20,
                animate = animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale = animation.Animation(400, curve = 'decelerate'),
                padding = padding.only(
                    top = 50,
                    left = 20,
                    right = 20,
                    bottom = 5
                ),
                content = Column(
                    controls = [
                        first_page_contents
                    ]
                )
            )
        ]
    )

    container = Container(
        width = 400,
        height = 850,
        bgcolor = BG,
        border_radius = 20,

        content = Stack(
            controls = [
                page_1,
                page_2
            ]
        )
    )

    create_tuition_view = Container(
        content =
         Container(
            height = 850,
            width = 400,
            bgcolor = BG,
            border_radius = 20,
            content = Column(
                controls = [
                    Stack(
                        controls = [
                            FloatingActionButton(
                                top = 20,
                                left = 20,
                                icon = icons.HOME, 
                                on_click = lambda _: page.go('/'),
                                bgcolor = LIGHTSTEELBLUE
                            ),
                        ]
                    ),
                ]
            )
         )
    )

    pages = {
        '/': View("/", [container]),
        '/create_tuition': View("/create_tuition", [create_tuition_view])
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