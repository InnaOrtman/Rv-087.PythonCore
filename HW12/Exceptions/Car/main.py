import Car

a = Car.Car()
b = Car.Car()

print("BOARD")
for i in Car.Car.board:
    print(i)

a.refill(10)
a.move(2,2)
b.refill(10)
b.move(2,2)

print("BOARD")
for i in Car.Car.board:
    print(i)
