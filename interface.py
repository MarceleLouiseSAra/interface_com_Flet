import time
from flet import *
from custom_checkbox import CustomCheckBox
import requests

# def request_data(event):
#     r = requests.post('http://localhost:8000/users')
#     print(r.json())

def main(page: Page):
    
    page.title = "aplicativo muito massa"
    page.theme_mode = 'dark'

    DEEPBLUE = '#432350'
    MEDIUMBLUE = '#b476ff'
    PINK = '#f4c9fd'
    WHITE = '#ffffff'
    LIGHTBLUE = '#B0C4DE'

    def shrink(e):
        home_page_1.controls[0].width = 200
        home_page_1.controls[0].scale = transform.Scale(
            0.8,
            alignment = alignment.center_right
        )
        home_page_1.controls[0].border_radius = border_radius.only(
            top_left = 20,
            top_right = 0,
            bottom_left = 20,
            bottom_right = 0
        )
        home_page_1.update()

    def restore(e):
        home_page_1.controls[0].width = 400
        home_page_1.controls[0].border_radius = 20
        home_page_1.controls[0].scale = transform.Scale(
            1,
            alignment = alignment.center_right
        )
        home_page_1.update()



    circle = Stack(
        controls = [
            Container(
                width = 100,
                height = 100,
                border_radius = 50,
                bgcolor = LIGHTBLUE
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
                            bgcolor = DEEPBLUE,
                            width = 90,
                            height = 90,
                            border_radius = 50,
                            content = Container(
                                bgcolor = MEDIUMBLUE,
                                height = 80,
                                width = 80,
                                border_radius = 40,
                                content = CircleAvatar(
                                    opacity = 0.8,
                                    foreground_image_url = "https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8MEDIUMBLUEVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
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
                bgcolor = DEEPBLUE,
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

    selected_group_ref = Ref[Text]()

    for group in groups:
        groups_card.controls.append(
            Container(
                width = 150,
                height = 90,
                border_radius = 10,
                bgcolor = DEEPBLUE,
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
                            bgcolor = LIGHTBLUE,
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

    waiting_room_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,
        margin = 10,
        padding = 10,
        alignment = alignment.center,

        content = Column(
            controls = [
                Column([
                    Container(
                        content = Text(
                            value = "fazAConta", 
                            size = 28, 
                            weight = 'bold', 
                            color = LIGHTBLUE
                        ),
                        margin = margin.only(top = 100, left = 35)
                    ),
                    Row([
                        Container(
                            width = 150,
                            content = TextButton(
                                "Criar conta",
                                style = ButtonStyle(
                                    bgcolor = MEDIUMBLUE,
                                    color = {
                                        ControlState.HOVERED: WHITE,
                                        ControlState.FOCUSED: MEDIUMBLUE,
                                        ControlState.DEFAULT: DEEPBLUE,
                                    }
                                ),
                                on_click = lambda _: page.go('/sign_in_page'),
                            ),
                            margin = margin.only(top = 400, left = 35)
                        ),
                        Container(
                            width = 150,
                            content = TextButton(
                                "Entrar",
                                style = ButtonStyle(
                                    bgcolor = MEDIUMBLUE,
                                    color = {
                                        ControlState.HOVERED: WHITE,
                                        ControlState.FOCUSED: MEDIUMBLUE,
                                        ControlState.DEFAULT: DEEPBLUE,
                                    }
                                ),
                                on_click = lambda _: page.go('/log_in_page'),
                            ),
                            margin = margin.only(top = 400, left = 5)
                        )
                    ])
                ])
            ],
        )
    )

    log_in_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,
        margin = 10,
        padding = 10,
        alignment = alignment.center,

        content = Column(
            width = 400,
            controls = [
                Row([
                    Container(
                        Icon(icons.ARROW_BACK_IOS_NEW_ROUNDED, color = LIGHTBLUE),
                        margin = margin.only(left = 15, right = 10, top = 20),
                        on_click = lambda _: page.go('/'),
                    ),
                    Container(
                        width = 100,
                        margin = margin.only(left = 215, right = 10, top = 20),
                        content = TextButton(
                            "Criar conta",
                            style = ButtonStyle(
                                color = LIGHTBLUE,
                                bgcolor = DEEPBLUE
                            ),
                            on_click = lambda _: page.go('/sign_in_page'),
                        ),
                    )
                ]),
                Container(
                    width = 400,
                    margin = margin.only(left = 150, right = 10, top = 30),
                    content = Text(
                        "Log in",
                        size = 30,
                        color = LIGHTBLUE,
                        weight = 'w700'
                    )
                ),
                Container(
                    width = 400,
                    margin = margin.only(left = 10, right = 10, top = 30),
                    alignment = alignment.center,
                    content = Text(
                        "Por favor, preencha as informações a seguir:",
                        size = 16,
                        color = LIGHTBLUE,
                        text_align = "center"
                    )
                ),
                Container(
                    width = 400,
                    margin = margin.only(left = 20, right = 20, top = 30),
                    content = Column(
                        controls = [
                            TextField(
                                label = "Nome de usuário",
                                hint_text = "Insira aqui o seu nome de usuário: ",
                                border_color = MEDIUMBLUE,
                                text_style = TextStyle(
                                    color = MEDIUMBLUE
                                ),
                                focused_border_color = PINK
                            )
                        ]
                    )
                ),
                Container(
                    width = 400,
                    margin = margin.only(left = 20, right = 20, top = 15),
                    content = Column(
                        controls = [
                            TextField(
                                label = "Senha",
                                hint_text = "Insira a sua senha aqui: ",
                                password = True,
                                can_reveal_password = True,
                                border_color = MEDIUMBLUE,
                                text_style = TextStyle(
                                    color = MEDIUMBLUE
                                ),
                                focused_border_color = PINK
                            )
                        ]
                    )
                ),
                Container(
                    width = 200,
                    margin = margin.only(left = 90, right = 20, top = 15),
                    content = TextButton(
                        "Esqueceu a senha?"
                    )
                ),
                Container(
                    width = 100,
                    margin = margin.only(left = 140, right = 20, top = 10),
                    content = TextButton(
                        "Entrar",
                        style = ButtonStyle(
                            color = {
                                ControlState.HOVERED: LIGHTBLUE,
                                ControlState.FOCUSED: WHITE,
                                ControlState.DEFAULT: PINK,
                            },
                            bgcolor = MEDIUMBLUE
                        ),
                        on_click = lambda _: page.go('/home_page')
                    )
                )
            ]
        )
    )

    user_name_field = TextField(
        label = "Nome de usuário",
        hint_text = "Insira aqui o seu nome de usuário: ",
        border_color = MEDIUMBLUE,
        text_style = TextStyle(
            color = MEDIUMBLUE
        ),
        focused_border_color = PINK
    )
    email_field = TextField(
        label = "E-mail",
        hint_text = "Insira aqui o seu e-mail: ",
        border_color = MEDIUMBLUE,
        text_style = TextStyle(
            color = MEDIUMBLUE
        ),
        focused_border_color = PINK
    )
    password_field = TextField(
        label = "Senha",
        hint_text = "Insira a sua senha aqui: ",
        password = True,
        can_reveal_password = True,
        border_color = MEDIUMBLUE,
        text_style = TextStyle(
            color = MEDIUMBLUE
        ),
        focused_border_color = PINK
    )


    def request_data(event):
        user_name = user_name_field.value
        email = email_field.value
        password = password_field.value
        

        body = {
            "user_name": user_name,
            "email": email,
            "password": password
        }
        r = requests.post('http://localhost:8000/users', data=body)
        print(r.json())



    sign_in_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,
        margin = 10,
        padding = 10,
        alignment = alignment.center,

        content = Column(
            width = 400,
            controls = [
                Row([
                    Container(
                        Icon(icons.ARROW_BACK_IOS_NEW_ROUNDED, color = LIGHTBLUE),
                        margin = margin.only(left = 15, right = 10, top = 20),
                        on_click = lambda _: page.go('/'),
                    ),
                    Container(
                        width = 100,
                        margin = margin.only(left = 215, right = 10, top = 20),
                        content = TextButton(
                            "Log in",
                            style = ButtonStyle(
                                color = LIGHTBLUE,
                                bgcolor = DEEPBLUE
                            ),
                            on_click = lambda _: page.go('/log_in_page'),
                        )
                    )
                ]),
                Container(
                    width = 400,
                    margin = margin.only(left = 120, right = 10, top = 30),
                    content = Text(
                        "Criar conta",
                        size = 30,
                        color = LIGHTBLUE,
                        weight = 'w700'
                    )
                ),
                Container(
                    width = 400,
                    margin = margin.only(left = 10, right = 10, top = 30),
                    alignment = alignment.center,
                    content = Text(
                        "Por favor, preencha as informações a seguir:",
                        size = 16,
                        color = LIGHTBLUE,
                        text_align = "center"
                    )
                ),
                Container(
                    width = 400,
                    margin = margin.only(left = 20, right = 20, top = 30),
                    content = Column(
                        controls = [user_name_field]
                    )
                ),
                Container(
                    width = 400,
                    margin = margin.only(left = 20, right = 20, top = 15),
                    content = Column(
                        controls = [email_field]
                    )
                ),
                Container(
                    width = 400,
                    margin = margin.only(left = 20, right = 20, top = 15),
                    content = Column(
                        controls = [
                            password_field,
                            TextField(
                                label = "Confirmar senha",
                                hint_text = "Insira a novamente a senha: ",
                                password = True,
                                can_reveal_password = False,
                                border_color = MEDIUMBLUE,
                                text_style = TextStyle(
                                    color = MEDIUMBLUE
                                ),
                                focused_border_color = PINK
                            )
                        ]
                    )
                ),
                Container(
                    width = 100,
                    margin = margin.only(left = 140, right = 20, top = 10),
                    content = TextButton(
                        "Criar conta",
                        style = ButtonStyle(
                            color = {
                                ControlState.HOVERED: LIGHTBLUE,
                                ControlState.FOCUSED: WHITE,
                                ControlState.DEFAULT: PINK,
                            },
                            bgcolor = MEDIUMBLUE
                        ),
                        on_click = lambda e: request_data(e)
                    )
                )
            ]
        )
    )

    first_page_contents = Container(
        content = Column(
            controls = [
                Row(
                    alignment = 'spaceBetween',
                    controls = [
                        Container(
                            on_click = lambda e: shrink(e),
                            # on_click = request_data,
                            content = Icon(icons.MENU, color = WHITE)
                        ),
                        Row(
                            controls = [
                                Container(
                                    Icon(icons.SEARCH, color = WHITE),
                                    # 
                                ),
                                Container(
                                    Icon(icons.NOTIFICATIONS_OUTLINED, color = WHITE),
                                    on_click = lambda _: page.go('/'),
                                ),
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
                            on_click = lambda _: page.go('/create_tuition_page'),
                            # on_click = lambda e: alertDialog(page),
                            bgcolor = LIGHTBLUE
                        )
                    ]
                )
            ]
        )
    )

    home_page_1 = Row(
        alignment = 'end',
        controls = [
            Container(
                width = 400,
                height = 850,
                bgcolor = MEDIUMBLUE,
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

    home_page_2 = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
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
                            bgcolor = LIGHTBLUE
                        ),
                    ]
                ),
                Container(
                    height = 20,
                ),
                circle,
                Text('João\nPirajá', size = 32, weight = 'bold', color = LIGHTBLUE),
                Container(
                    height = 5
                ),
                Container(
                    content = Column(
                        controls = [
                            Row(
                                controls = [
                                    Container(
                                        on_click = lambda _: page.go('/'),
                                        content = Icon(icons.ACCOUNT_CIRCLE_ROUNDED, color = LIGHTBLUE)
                                    ),
                                    Text(
                                        'Minha conta',
                                        color = LIGHTBLUE,
                                        weight = FontWeight.W_300,
                                        font_family = 'poppins'
                                    )
                                ]
                            ),
                            Row(
                                controls = [
                                    Container(
                                        on_click = lambda _: page.go('/'),
                                        content = Icon(icons.ADMIN_PANEL_SETTINGS_ROUNDED, color = LIGHTBLUE),
                                    ),
                                        Text(
                                            'Configurações',
                                            color = LIGHTBLUE,
                                            weight = FontWeight.W_300,
                                            font_family = 'poppins',
                                        )
                                ]
                            ),
                            Row(
                                controls = [
                                    Container(
                                        on_click = lambda _: page.go('/'),
                                        content = Icon(icons.ARROW_BACK_IOS_NEW_ROUNDED, color = LIGHTBLUE)
                                    ),
                                    Text(
                                        'Sair',
                                        color = LIGHTBLUE,
                                        weight = FontWeight.W_300,
                                        font_family = 'poppins'
                                    )
                                ]
                            ),
                        ]
                    )
                ),
            ]
        )
    )

    home_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,

        content = Stack(
            controls = [
                home_page_2,
                home_page_1
            ]
        )
    )

    create_tuition_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,
        padding = padding.only(left = 30, top = 30, right = 30),

        content = Column(
            controls = [
                Stack(
                    controls = [
                        FloatingActionButton(
                            icon = icons.HOME, 
                            on_click = lambda _: page.go('/home_page'),
                            bgcolor = LIGHTBLUE
                        )
                    ],
                ),
                Container(
                    alignment = alignment.center,
                    padding = padding.only(top = 30),
                    content = Text(
                        "Criar despesa",
                        size = 30,
                        color = LIGHTBLUE,
                        weight = 'w700'
                    )
                ),
                Container(
                    alignment = alignment.center,
                    padding = padding.only(top = 15),
                    content = Text(
                        "Por favor, preencha as informações a seguir:",
                        size = 16,
                        color = LIGHTBLUE,
                        text_align = "center"
                    )
                ),
                Container(
                    padding = padding.only(top = 10),
                    content = Column(
                        controls = [
                            TextField(
                                label = "Nome da despesa",
                                hint_text = "Insira aqui o nome da despesa: ",
                                border_color = MEDIUMBLUE,
                                text_style = TextStyle(
                                    color = MEDIUMBLUE
                                ),
                                focused_border_color = PINK
                            )
                        ]
                    )
                ),
                Container(
                    padding = padding.only(top = 10),
                    content = Column(
                        controls = [
                            TextField(
                                label = "Valor da despesa",
                                hint_text = "Quanto esta despesa custou?: ",
                                border_color = MEDIUMBLUE,
                                text_style = TextStyle(
                                    color = MEDIUMBLUE
                                ),
                                focused_border_color = PINK
                            )
                        ]
                    )
                ),
                # Container(
                #     padding = padding.only(top = 10),
                #     content = Column(
                #         controls=[
                #             Text("Grupo da despesa:", size = 16),
                #             TextButton(
                #                 content = Text(value = groups[2], ref = selected_group_ref, size = 16),
                #                 style = ButtonStyle(color = MEDIUMBLUE),
                #                 on_click = lambda e: page.open(
                #                     CupertinoBottomSheet(
                #                         cupertino_picker,
                #                         height = 216,
                #                         padding = padding.only(top=6),
                #                     )
                #                 ),
                #             ),
                #         ],
                #     )
                # ),
                Container(
                    padding = padding.only(top = 10),
                    content = Column(
                        controls = [
                            TextField(
                                label = "Senha",
                                hint_text = "Insira a sua senha aqui: ",
                                password = True,
                                can_reveal_password = True,
                                border_color = MEDIUMBLUE,
                                text_style = TextStyle(
                                    color = MEDIUMBLUE
                                ),
                                focused_border_color = PINK
                            )
                        ]
                    )
                ),
                Container(
                    alignment = alignment.center,
                    padding = padding.only(top = 10),
                    content = TextButton(
                        "Criar despesa",
                        style = ButtonStyle(
                            color = {
                                ControlState.HOVERED: LIGHTBLUE,
                                ControlState.FOCUSED: WHITE,
                                ControlState.DEFAULT: PINK,
                            },
                            bgcolor = MEDIUMBLUE
                        ),
                        # on_click = lambda e: inserirDados(e)
                    )
                )
            ]
        )
    )

    pages = {
        '/': View("/waiting_room_page", [waiting_room_page]),
        '/log_in_page': View("/log_in_page", [log_in_page]),
        '/sign_in_page': View("/sign_in_page", [sign_in_page]),
        '/home_page': View("/home_page", [home_page]),
        '/create_tuition_page': View("/create_tuition_page", [create_tuition_page])
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