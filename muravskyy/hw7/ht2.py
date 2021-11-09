symbol_a = '123A12AbbcaA78zzAttya23J890'
symbol_b = '23999hbbcaA7kdmURHD78MVNMcv'
a = {x for x in symbol_a if not str(x).isnumeric()}
b = {x for x in symbol_b if not str(x).isnumeric()}
print(f'letters are in both = {sorted(a.intersection(b))}')
print(f'letters are only firs {sorted(a.difference(b))}')
print(f'letters are only firs {sorted(b.difference(a))}')