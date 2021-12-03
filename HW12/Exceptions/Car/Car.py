import Car_exceptions
import Point


class Car:
    board = []
    def __init__(self, model = "Toyota", fuel_amount: float = 1.0, fuel_capacity: int = 100, fuel_consumption: float = 1.0, loc_x = 0, loc_y = 0):
        self.location = Point.Point(0,0)
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
        self.refill(fuel_amount)
        self.fuel_consumption = fuel_consumption

        Car.board.append(self.location)


    def __str__(self):
        return f"Model name: {self.model}\n\
Fuel: {self.fuel_amount}/ {self.fuel_capacity}\n\
Consumption: {self.fuel_consumption}\n\
location: {self.location}"

    def refill(self, amount: float = 1):
        try:
            if (self.fuel_amount + amount) > self.fuel_capacity:
                raise Car_exceptions.TooMuchFuelError
            elif amount < 1:
                raise NotEnoughFuelError
        except (Car_exceptions.TooMuchFuelError, Car_exception.NotEnoughFuelError) as e:
            print(e.message)
        else:
            print("Refuelled successfully.")
            self.fuel_amount += amount

    def move(self, x, y):
        print(f"Trying to move to ({x}, {y})")
        destination = Point.Point(x,y)
        try:
            if self.location == destination or destination in Car.board:
                raise Car_exceptions.SpaceOccupiedError
            elif destination.x < 0 or destination.y < 0:
                raise Point.NegativeCoordsError
            # GETS CALCULATED TWICE, HOW TO FIX?
            else:
                distance = round(self.location.distance_to(destination),2)
                print(f"Distance to travel: {distance}")
                if self.fuel_consumption * distance <= self.fuel_amount:
                    if self.location in Car.board:
                        Car.board[Car.board.index(self.location)] = destination
                    self.location = destination
                    self.fuel_amount = round(self.fuel_amount - self.fuel_consumption * distance, 2)
                else:
                    raise Car_exceptions.OutOfFuelError
        except (Car_exceptions.SpaceOccupiedError, Point.NegativeCoordsError, Car_exceptions.OutOfFuelError) as e:
            print(e.message)