def calc_pos(*args):
    positive = 0
    for i in args[0]:
        if i <0:
            positive += 1
    return positive

positive = 0
negative = 0
x  = -5
args = []
while len(args) < 10:
    args.append(x)
    x += 1

# print(f"There are {total} numbers entered, {positive / total * 100}% are positive, {negative / total * 100}% are negative.")