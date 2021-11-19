class ClosedDoor:
    """THis is door class."""

    color = ""
    state = ""

    def __init__(self, state="closed"):
        self.state = state



door = ClosedDoor()

print(door.state)