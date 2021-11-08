input_string = str("Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\
Vivamus a orci consectetur, accumsan libero quis, porttitor odio.\n\
Vestibulum porta massa vel dui sollicitudin, at efficitur ipsum lobortis.\n\
Etiam commodo a tellus vel sollicitudin. Praesent\
at risus at nunc rhoncus posuere non id ligula.\n\
Aenean rutrum ipsum lacus, sed pretium ante dictum non.")

uniques_set = set(input_string.lower().split())
resulting_dict = {}
for i in uniques_set:
    if i not in resulting_dict.keys():
        resulting_dict[i] = list(input_string.lower().split()).count(i)

for i, j in resulting_dict.items():
    print(f"{i}: {j}")
