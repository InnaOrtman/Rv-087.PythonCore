s = float(input('Enter area of square hall:'))
r = float(input('Enter stage radius'))
k = float(input('Enter needed passage'))
print(f'You will have enough space for passage'\
      if r < s**(1/2) and (s**(1/2) - r) > k\
      else 'Yoy will not have enough spase for passage')
