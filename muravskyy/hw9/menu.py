class Menu:
    gameMenu = '              GAME FISHING\n\n' \
                   '1. View capacity\n' \
                   '2. View state of Pond\n' \
                   '3. Add fish( Carp or SheatFish)\n' \
                   '4. Catch fish\n' \
                   '0. Finish the game.\n' 
    msgAddFish = '  Enter the number of fish\n\n' \
                    '1. Carp\n' \
                    '2. SeatFich\n'
    msgWeight = 'enter the weigth\n'
    msgColor = 'enter the color from list\n'
    msglenght = 'enter the whisckerlenght\n'
    msgLostFish = 'choose the fish\n'
    msgViewPond = 'state of the pond:'
    def msgReturn(a=''):
        return input(f'\t{a}\n\tpress ''ENTER'' for return')