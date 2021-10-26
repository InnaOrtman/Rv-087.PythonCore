import math

ticket = int(input('choose your seat (available up 54)\t'))


if ticket % 2 != 0:
    if ticket < 37:
        c = math.ceil(ticket / 4)
        seat = ('botton and compartment')
        print()
    else:
        seat = ('botton and outside') 
        c = ''  
else:
    if ticket < 37:        
        seat = ('top and compartment')
        c = math.ceil(ticket / 4)
    else:
        seat = ('top and outside') 
        c = ''
seat = 'your place is '+seat        
print(seat,c)