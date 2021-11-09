import random


k_list = []
r_list = [random.randint(0, 100) for x in range(5)]

while len(k_list) < 5:
    k_list.append(int(input()))    
sum_list = [x+y for x,y in zip(k_list, r_list)]
print(f'{k_list}\n{r_list}\n{sum_list}')