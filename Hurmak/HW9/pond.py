class Pond:

    def __init__(self, capacity = None):
        self.status = ''
        if capacity is None:
            self.capacity = []
        else:
            self.capacity = capacity

    def checkStatus(self):
        if len(self.capacity) < 5:
            self.status = 'poor'
        elif len(self.capacity) > 10:
            self.status = 'rich'
        else:
            self.status = 'normal'

    def obtainFish(self, fish):
        self.capacity.append(fish)
        Pond.checkStatus(self)

    def lostFish(self, fish):
        if fish in self.capacity:
            self.capacity.remove(fish)
            Pond.checkStatus(self)

    def showStatus(self):
        return self.status
