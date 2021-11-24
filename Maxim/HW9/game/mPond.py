class Pond:
    """Pond. It should have the next attributes: capacity –
    list that contains all fish from the Pond in the current moment;
    state – ‘poor’, ‘normal’, ‘rich’. Pond is ‘poor’ if it’s capacity
    contains less then 5 fishes, ‘normal’, if capacity contains
    from 5 to 10 fishes, and ‘rich’ if it has more than 10 fishes.
    Pond can obtainFish() – it will be added to it’s capacity,
    and lostFish() – it will be taken from capacity. The Pond state
    changes automatically when it’s capacity reaches the appropriate
    value. Pond also allows showPapacity() and showState(). You can
    also add the optional attributes (as you wish)."""

    def __init__(self):
        self.capacity = []
        self.state = "The pond is empty"

    def showCapacity(self):
        lst = []
        for i in range(len(self.capacity)):
            if self.capacity[i].feature is None:
                lst.append(f"{self.capacity[i].name} weight: "
                           f"{self.capacity[i].weight}")
            else:
                lst.append(f"{self.capacity[i].name} weight: "
                           f"{self.capacity[i].weight} "
                           f"{self.capacity[i].feature}")
        return lst

    def showState(self):
        return self.state

    def chageState(self):
        lenCapacity = len(self.capacity)
        if lenCapacity:
            if lenCapacity < 5:
                self.state = "poor"
            elif 4 < lenCapacity < 11:
                self.state = "normal"
            else:
                self.state = "rich"
        else:
            self.state = "The pond is empty"

    def obtainFish(self, obj):
        self.capacity.append(obj)
        self.chageState()

    def lostFish(self, fish: str):
        for i in range(len(self.capacity)):
            if self.capacity[i].name == fish:
                tmp = self.capacity[i]
                del self.capacity[i]
                self.chageState()
                return tmp
        return False
