import random
S=random.randint(10,100)
print("S="+str(S))
R=random.randint(10,100)
print("R="+str(R))
K=random.randint(1,10)
print("K="+str(K))
if S-K>R :
    print("In the hall you can put the scene")
if S-K<=R:
    print("In the hall it is impossible to place a scene")