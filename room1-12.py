rooms = {
    'room_1':{'south': 'room_2', 'east': 'room_3'},
    'room_2':{'south': 'gambling_2', 'north': 'room_1'},
    'room_3':{'north': 'room_4', 'east': 'gambling_1'},
    'Room_4':{'west' : 'room_1', 'south': 'room_3'},
    'room_5':{'east': 'room_7', 'west': 'gambling_1'},
    'room_6':{'north': 'gambling_1', 'south': 'room_9', 'east': 'CRY_PEASANTS', 'west': 'CRY_PEASANTS'},
    'room_7':{'south': 'CRY_PEASANTS', 'west': 'room_5'},
    'room_8':{'east': 'room_9', 'west': 'gambling_2'},
    'room_9':{'east': 'room_10', 'north' : 'room_6', 'west' : 'room_8'},
    'room_10':{'west': 'room_9'},
    'CRY_PEASANTS':{'north': 'room_1', 'south': 'room_1', 'east': 'room_1', 'west': 'room_1'}
}

def show_instructions():
    print('The instructions are as follows: north, south, east, west')

def everything_rooms_1():
    def move_rooms_1(direction, room='room_1'):
        if direction == 'south':
            room = 'room_1'
            return rooms[room]['south']
        elif direction == 'north':
            if room == 'room_1':
                return 'Invalid direction please try again.'
            return rooms[room]['north']
        elif direction == 'east':
            room == 'room_3'
            return rooms[room]['east']
        elif direction == 'west':
            if room == 'room_1':
                return 'Invalid direction please try again.'
            return rooms[room]['west']
        
    currentRoom = 'room_1'
    gameInstructions = 'The instructions are as follows:north,south, east, west'
    print(gameInstructions)
    print(currentRoom)
        

    userDirection = ''
    while userDirection != 'exit':
        userDirection = input("Pick a direction, or MUST type exit to exit the game.")
        if currentRoom == 'room_1':
            if userDirection == 'south':
                currentRoom = move_rooms_1(userDirection, currentRoom)
                show_instructions()
                print(currentRoom)
            elif userDirection == 'east':
                currentRoom = move_rooms_1(userDirection, currentRoom)
                show_instructions()
                print(currentRoom)
        else:
            print('That is not a direction, pick another direction.')
            print(currentRoom)
            show_instructions()

def everything_rooms_2():
    def move_rooms_2(direction, room='room_2'):
        if direction == 'south':
            room = 'gambling_2'
            return rooms['room_2']['south']
        elif direction == 'north':
            room = 'room_1'
            return rooms['room_1']['north']
        elif direction == 'east':
            if room == 'room_2':
                return 'Invalid direction please try again.'
            return rooms[room]['east']
        elif direction == 'west':
            if room == 'room_2':
                return 'Invalid direction please try again.'
            return rooms[room]['west']
        
    currentRoom = 'room_2'
    gameInstructions = 'to ways to go are north, south, east, west'
    print(gameInstructions)
    print(currentRoom)

    userDirection = ''
    while userDirection != 'exit':
        userDirection = input("Pick a direction, or MUST type exit to exit the game.")
        if currentRoom == 'room_2':
            if userDirection == 'south':
                currentRoom = move_rooms_2(userDirection, currentRoom)
                show_instructions()
                print(currentRoom)
            elif userDirection == 'north':
                currentRoom = move_rooms_2(userDirection, currentRoom)
                show_instructions()
                print(currentRoom)
        else:
            print('That is not a direction, pick another direction.')
            print(currentRoom)
            show_instructions()

def everything_rooms_3():
    def move_rooms_3(direction, room='room_3'):
        if direction == 'south':
            if room == 'room_3':
                return 'Invalid direction please try again.'
            return rooms[room]['south']
        elif direction == 'north':
            room == 'room_4'
            return rooms[room]['north']
        elif direction == 'east':
            room == 'gambling_1'
            return rooms[room]['east']
        elif direction == 'west':
            if room == 'room_3':
                return 'Invalid direction please try again.'
            return rooms[room]['west']
        
    currentRoom = 'room_3'
    gameInstructions = 'to ways to go are north, south, east, west'
    print(gameInstructions)
    print(currentRoom)

    userDirection = ''
    while userDirection != 'exit':
        userDirection = input("Pick a direction, or MUST type exit to exit the game.")
        if currentRoom == 'room_3':
            if userDirection == 'north':
                currentRoom = move_rooms_3(userDirection, currentRoom)
                show_instructions()
                print(currentRoom)
            elif userDirection == 'east':
                currentRoom = move_rooms_3(userDirection, currentRoom)
                show_instructions()
                print(currentRoom)
        else:
            print('That is not a direction, pick another direction.')
            print(currentRoom)
            show_instructions()

def everything_room_4():
    def move_rooms_4(direction, room='room_4'):
        if direction == 'south':
            room == 'room_3'
            return rooms[room]['south']
        elif direction == 'north':
            if room == 'room_4':
                return 'Invalid direction please try again.'
            return rooms[room]['north']
        elif direction == 'east':
            if room == 'room_4':
                return 'Invalid direction please try again.'
            return rooms[room]['east']
        elif direction == 'west':
            room == 'room_1'
            return rooms[room]['west']
    
    currentRoom = 'room_4'
    gameInstructions = 'to ways to go are north, south, east, west'
    print(gameInstructions)
    print(currentRoom)

    userDirection = ''
    while userDirection != 'exit':
        userDirection = input("Pick a direction, or MUST type exit to exit the game.")
        if currentRoom == 'room_4':
            if userDirection == 'west':
                currentRoom = move_rooms_4(userDirection, currentRoom)
                show_instructions()
                print(currentRoom)
            elif userDirection == 'south':
                currentRoom = move_rooms_4(userDirection, currentRoom)
                show_instructions()
                print(currentRoom)
        else:
            print('That is not a direction, pick another direction.')
            print(currentRoom)
            show_instructions()

def everything_rooms_5():
    def move_rooms_5(direction, room='room_5'):
        if direction == 'south':
            if room == 'room_5':
                return 'Invalid direction please try again.'
            return rooms[room]['south']
        elif direction == 'north':
            if room == 'room_5':
                return 'Invalid direction please try again.'
            return rooms[room]['north']
        elif direction == 'east':
            room == 'room_7'
            return rooms[room]['east']
        elif direction == 'west':
            room == 'gambling_1'
            return rooms[room]['west']
    
    currentRoom = 'room_5'
    gameInstructions = 'to ways to go are north, south, east, west'
    print(gameInstructions)
    print(currentRoom)

    userDirection = ''
    while userDirection != 'exit':
        userDirection = input("Pick a direction, or MUST type exit to exit the game.")
        if currentRoom == 'room_5':
            if userDirection == 'west':
                currentRoom = move_rooms_5(userDirection, currentRoom)
                show_instructions()
                print(currentRoom)
            elif userDirection == 'east':
                currentRoom = move_rooms_5(userDirection, currentRoom)
                show_instructions()
                print(currentRoom)
        else:
            print('That is not a direction, pick another direction.')
            print(currentRoom)
            show_instructions()