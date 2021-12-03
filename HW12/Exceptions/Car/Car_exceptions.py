class TooMuchFuelError(Exception):
    def __init__(self, message="You tried to add too much fuel."):
        self.message = message


class NotEnoughFuelError(Exception):
    def __init__(self, message="To tried to add too few fuel."):
        self.message = message


class OutOfFuelError(Exception):
    def __init__(self, message="Out of fuel"):
        self.message = message


class SpaceOccupiedError(Exception):
    def __init__(self, message="This spot is already occupied."):
        self.message = message


class FuelAmountLessOne(Exception):
    def __init__(self, message="You can't add negative fuel amount"):
        self.message = message

