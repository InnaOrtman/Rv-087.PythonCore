import random

SAMPLE_SIZE = 10
rand_list = []
input_list = []

for i in range(SAMPLE_SIZE):
    rand_list.append(random.randint(0, 1001))
    
while len(input_list) != SAMPLE_SIZE:
    try:
        x = (int(input(f"Please enter an integer. {SAMPLE_SIZE - len(input_list)} left to enter. \n")))
    except (ValueError):
        print("Please enter integers only")
    else:
        input_list.append(x)

resulting_list = sum(rand_list + input_list)

print(resulting_list)
