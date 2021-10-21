ticket = int(input('choose your seat (available up 54)\t'))


seat = ''
if ticket % 2 != 0:
    if ticket < 37:
        seat = ('botton and compartment')
    else:
        seat = ('botton and outside')    
else:
    if ticket < 37:        
        seat = ('top and compartment')
    else:
        seat = ('top and outside') 

seat = 'your place is '+seat        
print(seat)