def bank(n , years:int):
    for x in range(years):
        n += n*0.1
    return round(n, 2)

print(f'your deposite will increase to \
{bank(100, 5)} $')