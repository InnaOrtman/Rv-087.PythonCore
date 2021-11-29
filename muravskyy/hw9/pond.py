class Pond:
    def __init__(self):
        self.capacity = {}
        self.state = ''

    def obtainFish(self,name,value):
        self.capacity[name] = value

    def lostFish(self,name):
        self.capacity.pop(name)

    def showState(self):
        if len(self.capacity) < 5:
            self.state = 'poor'
        elif len(self.capacity) > 10:
            self.state = 'rich'
        else:
            self.state = 'normal'
        print(f'state of the Pond is {self.state}')

    def showCapacity(self):
        print('\nThere are\n')
        for x in self.capacity.items():
            print(x)