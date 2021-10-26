# task_4
import math
R = int(input("Enter the radius of the circle: "))
S = int(input("Enter the area of the square: "))
K = int(input("Enter the passage from the wall to the stage: "))

if math.sqrt(S) >= (R*2+K):
    print("Yes")
else:
    print("No")



