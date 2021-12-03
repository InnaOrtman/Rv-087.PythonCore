from math import hypot, sqrt

sideA = 10
sideB = 10

hypothenuse_manual = sqrt(pow(sideA, 2) + pow(sideB, 2))
hypothenuse_auto = hypot(sideA, sideB)

def hypot_manual(sideA, sideB):
    return sqrt(pow(sideA, 2) + pow(sideB, 2))

print(f"Manual, hypot = {hypothenuse_manual}\n")
print(f"Auto, hypot = {hypothenuse_auto}\n")

