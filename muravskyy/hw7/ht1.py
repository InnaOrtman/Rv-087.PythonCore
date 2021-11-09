def my_str(a):
    temp_list = []
    for i in range(len(a)):
        if a[i] != a[i-1]:
            temp_list.append(a[i])
    my_str = ''.join(temp_list)
    return my_str

input_values = '311165551s;::ldDkfs;;kd;++--32334'
print(f'{input_values}\n{my_str(input_values)}')