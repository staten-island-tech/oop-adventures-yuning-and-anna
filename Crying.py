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
    'room_10':{'west': 'room_9'}
}

def show_instructions():
    print('The way to move around in this dungeon are as follows: north, south, east, west')

def move_rooms(direction, room='room_1'):
    if direction == 'south':
        room = 'room_2'
        return rooms['room_2']['South']
    elif direction == 'north':
        if room == 'room_1':
            return 'Invalid direction please try again.'
        return rooms[room]['North']
    elif direction == 'east':
        room == 'room_3'
        return rooms[room]['East']
    elif direction == 'west':
        if room == 'room_1':
            return 'Invalid direction please try again.'
        return rooms[room]['West']

def move_room_1():
    userDirection = ''
    while userDirection != 'exit':
        userDirection = input("Pick a direction, or MUST type exit to exit the game.")
        if currentRoom == 'room_1':
            if userDirection == 'south':
                currentRoom = move_rooms(userDirection, currentRoom)
                show_instructions()
                print(currentRoom)
            elif userDirection == 'east':
                currentRoom = move_rooms(userDirection, currentRoom)
                show_instructions()
                print(currentRoom)
        else:
            print('Invalid direction. Please pick another direction.')
            print(currentRoom)
            show_instructions()

