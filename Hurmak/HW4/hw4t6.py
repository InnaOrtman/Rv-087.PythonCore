import random

place = random.randint(1,54)
if place%2 == 0:
    level = 'top'
else:
    level = 'bottom'
if place < 37:
    position = 'compartment'
else:
    position = 'side'
print(f"You've got {level} place in the {position} number {place}")
