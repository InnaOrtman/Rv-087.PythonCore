
SideSquareHall = float(input('enter side of square hall\t'))
RadiusRoundStage = float(input('enter radius round stage\t'))
PassageDistance = float(input('enter passage distance\t'))


if 2 * RadiusRoundStage > SideSquareHall - PassageDistance:
    print('impossible option !!!') 
else:    
    print('good choise !!!')