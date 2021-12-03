class NegativeCoordsError(Exception):
    def __init__(self, message="Sorry, coordinates can't be negative"):
        self.message = message


class WrongPointError(Exception):
    def __init__(self, message="Point should have two numeric coordinates only"):
        self.message = message
