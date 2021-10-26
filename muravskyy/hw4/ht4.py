SideSquareHall = float(input('enter side of square hall\t'))
PassageDistance = float(input('enter passage distance\t'))
RadiusRoundStage = float(input('enter radius round stage\t'))


if 2 * RadiusRoundStage > SideSquareHall - (2*PassageDistance):
    print('impossible option !!!') 
else:    
    print('good choise !!!')
    