import PySimpleGUI as sg
from fishes import *
from pond import *


def notInPondCeck(instances):
    ''' function return a list of available fishes '''
    notInPond = []
    for i in instances:
        if i not in boloto.capacity:
            notInPond.append(i)
    return notInPond


def createAFish(newFishClass, newFishWeight, newFishColorWis):
    ''' Will create a new fish according to selected species '''
    if newFishClass == 'Carp':
        return Carp(int(newFishWeight), newFishColorWis)
    else:
        return Sheatfish(int(newFishWeight), int(newFishColorWis))

if __name__ =='__main__':
    # let's fill our pond with water and name it
    boloto = Pond()

    # create some fishes and add to pound few of them
    carp1 = Carp(100, 'red')
    boloto.obtainFish(carp1)
    carp2 = Carp(200, 'yellow')
    boloto.obtainFish(carp2)
    carp3 = Carp(240, 'orange')
    sheatfish1 = Sheatfish(3500, 25)
    sheatfish2 = Sheatfish(1800, 20)
    sheatfish3 = Sheatfish(1600, 10)
    carp4 = Carp(340, 'orange')
    boloto.obtainFish(carp4)
    carp5 = Carp(140, 'white')
    carp6 = Carp(2500, 'gold')
    sheatfish4 = Sheatfish(1800, 25)
    sheatfish5 = Sheatfish(10600, 155)

    # GUI part
    # Forming layout for our GUI
    # Layout with elements of left part of window
    left_col = [[sg.Text('Available fishes:')],
                [sg.Listbox(values=notInPondCeck(Fish.instances), enable_events=True, size=(40,7),key='AV_LIST')],
                [sg.Button(button_text='Add fish to the pond --->', key='ADD_TO', size=(37, 1))],
                [sg.Text('Create new fish:')],
                [sg.Combo(size=(10, 2), values=[cls.__name__ for cls in Fish.__subclasses__()],
                          key='SPECIES', enable_events=True),
                sg.Input(size=(10, 1), default_text='Weight', disabled_readonly_text_color='grey',
                         disabled=True, key='INWEIGHT', enable_events=True),
                sg.Input(size=(15, 1), default_text='Color/Wisker', disabled_readonly_text_color='grey',
                         disabled=True, key='INCOWI', enable_events=True)],
                [sg.Button(button_text='Create new fish', key='CREATE_FISH', disabled=True, enable_events=True)],
                ]
    # Layout with elements of right part of window
    right_col = [[sg.Text('Fishes in the pond:')],
                 [sg.Listbox(values=boloto.capacity, enable_events=True, size=(40,10),key='POND_LIST')],
                 [sg.Text(text=f'Status: {boloto.showStatus()}', key='OUT')],
                 [sg.Button(button_text='Catch a fish', key='CATCH_BUT'), sg.Button(button_text='Quit', key='QUIT')]
                 ]

    # Whole layout: left + right parts with all elements and their properties separated with vertical bar
    layout = [[sg.Column(left_col), sg.VSeperator(), sg.Column(right_col)]]
    # Creating window on the screen with title and formed layout
    window = sg.Window('How much is the fish?...The chase is better than the catch', layout)

    # Main application loop. Will be running and processing all events while not press 'Quit' or close the window
    while True:
        event, values = window.read()
        print(event, values)
        # See if user wants to quit or window was closed, if not processing all other events
        if event == sg.WINDOW_CLOSED or event == 'QUIT':
            break
        # See if button "Add to pond" pressed
        elif event == 'ADD_TO':
            sel_add = values['AV_LIST'][0]
            boloto.obtainFish(sel_add)
            window['POND_LIST'].update(boloto.capacity)
            window['AV_LIST'].update(notInPondCeck(Fish.instances))
            window['OUT'].update(f'Status: {boloto.showStatus()}')
        # See if button "Catch fish" pressed
        elif event == 'CATCH_BUT':
            sel_pond=values['POND_LIST'][0]
            boloto.lostFish(sel_pond)
            del sel_pond
            window['POND_LIST'].update(boloto.capacity)
            window['OUT'].update(f'Status: {boloto.showStatus()}')
        # See if combo pressed. Set fish species and enable input fields with fish attributes
        elif event == 'SPECIES':
            window['INWEIGHT'].update(disabled=False,  text_color='black')
            if values['SPECIES'] == 'Carp':
                window['INCOWI'].update('Color',disabled=False, text_color='black')
                window['INWEIGHT'].update('Weight', disabled=False, text_color='black')
            else:
                window['INCOWI'].update('Wisker', disabled=False, text_color='black')
                window['INWEIGHT'].update('Weight', disabled=False, text_color='black')
            window['CREATE_FISH'].update(disabled=False)
        # See if 'Create Fish' button pressed.
        elif event == 'CREATE_FISH':
            createAFish(values['SPECIES'], values['INWEIGHT'], values['INCOWI'])
            window['AV_LIST'].update(notInPondCeck(Fish.instances))
            window['INWEIGHT']('')
            window['INCOWI']('')
            window['SPECIES']('')
            window['CREATE_FISH'].update(disabled=True)
