from enum import Enum


class Routes(str, Enum):
    HOME = "/"
    LOGIN = "/login"
    REGISTER = "/register"
    NOT_FOUND = "/not-found"

    @classmethod
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


# View props
VIEW_WIDTH = 400
VIEW_HEIGHT = 850
BORDER_RADIUS = 20

# Colors
DEEPBLUE = "#432350"
MEDIUMBLUE = "#b476ff"
PINK = "#f4c9fd"
WHITE = "#ffffff"
LIGHTBLUE = "#B0C4DE"
