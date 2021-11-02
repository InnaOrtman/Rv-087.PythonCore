def multiply(mylist):
    a = 1
    for x in mylist:
        a *= x
    return a

p = int(input('enter P\t'))
h = int(input('enter H\t'))


my_list = []
while True:
    number = int(input('enter a sequence of numbers\n'))
    my_list += [number]
    if number == p or number == h:
        break
list_less_p = [x for x in my_list if x < p]
list_more_h = [x for x in my_list if x > h]
list_p_h = [x for x in my_list if x in range(p, h + 1)]
print(f'sum of numbers are less P -\t {sum(list_less_p)}\nproduct of numbers greater than H -\t \
{multiply(list_p_h)}\nnumbers in the range P_H - \t{list_p_h}')