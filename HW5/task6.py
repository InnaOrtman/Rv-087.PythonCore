def calc_pos(*args):
    positive = 0

    for i in args:
        print(i)

    return positive

positive = 0
negative = 0

args = []
while len(args) < 10:
    args.append(int(input("Please enter number")))

positive = calc_pos(args)
negative = len(args) - positive


# print(f"There are {total} numbers entered, {positive / total * 100}% are positive, {negative / total * 100}% are negative.")