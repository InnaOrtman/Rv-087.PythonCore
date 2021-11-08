string1 = '12345AaBb'
string2 = '456789BbCc'
print(sorted(set(string1).union(set(string2))))
print(sorted(set(string1).intersection(set(string2))))
