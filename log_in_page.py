from flet import *
import requests

DEEPBLUE = '#432350'
MEDIUMBLUE = '#b476ff'
PINK = '#f4c9fd'
WHITE = '#ffffff'
LIGHTBLUE = '#B0C4DE'

page: Page

def view_log_in_page(page: Page) -> Container:


    username_input = TextField(
        label = "Usuário", 
        hint_text = "Insira aqui o nome de usuário: ",
        border_color = MEDIUMBLUE,
        text_style = TextStyle(
            color = LIGHTBLUE
        ),
        autofocus = True,
        focused_border_color = PINK
    )
    
    password_input = TextField(
        label = "Senha", 
        hint_text = "Insira aqui a senha: ",
        border_color = MEDIUMBLUE,
        text_style = TextStyle(
            color = LIGHTBLUE
        ),
        autofocus = True,
        password = True,
        can_reveal_password = True,
        focused_border_color = PINK
    )

    def on_submit(e): # análogo ao request_data
        username = username_input.value
        password = password_input.value
        # VALIDAÇÕES AQUI
        print(f"Usuário:", {username}, "Senha:", {password})
        page.go('/home_page')

    def request_data(e):
        user_name = username_input.value
        password = password_input.value
        
        body = {
            "user_name": user_name,
            "password": password
        }

        r = requests.get('http://localhost:8000/users', data = body)
        print(r.json())
        page.go('/home_page')

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
                        controls = [username_input]
                    )
                ),
                Container(
                    width = 400,
                    margin = margin.only(left = 20, right = 20, top = 15),
                    content = Column(
                        controls = [password_input]
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
                        on_click = lambda e: on_submit(e) # trocar pela request_data
                    )
                )
            ]
        )
    )

    return (log_in_page)