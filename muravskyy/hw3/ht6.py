import random
cats = ['Bengal', 'Bombay', 'Egyptian']
DescriptionCats = ['Usa', 'Thailand', 'Canada']
cars = ['Tayota', 'Bmw', 'Ford']
DescriptionCars = ['Japan', 'German', 'Usa']
elephants = ["India", "Tusked", "African"]
DescriptionElephants = ['1', '2', '3']

MarksCats = {k: d for k ,d in zip(cats, DescriptionCats)}
MarksCars = {k: d for k ,d in zip(cars, DescriptionCars)}
MarksElephants = {k: d for k ,d in zip(elephants, DescriptionElephants)}

collector1 = {'cars' : MarksCars , 'cats' : MarksCats}
collector2 = {'cars' : MarksCars , 'elephants' : MarksElephants}

collector2.update (collector1['cats']) 

# не можу зрозуміти як добавити не тільки dict в середині 'cats' 
       #  'Bengal': 'Usa', 'Bombay': 'Thailand', 'Egyptian': 'Canada'                               
#   а щоб  було  'cats' : {'Bengal': 'Usa', 'Bombay': 'Thailand', 'Egyptian': 'Canada' }
                                          
print(collector2)
