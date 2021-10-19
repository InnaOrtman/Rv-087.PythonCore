from math import hypot, sqrt

sideA = int(input("Please input side A length\n"))
sideB = int(input("Please input side B length\n"))

hypothenuse_manual = sqrt(pow(sideA, 2) + pow(sideB, 2))
hypothenuse_auto = hypot(sideA, sideB)

print(f"Manual, hypot = {hypothenuse_manual}\n")
print(f"Auto, hypot = {hypothenuse_auto}\n")

