# Make map that represent rooms,exits,items,puzzels and discription
# we used dictionary to nake the map
game_map = {
    'Entrance': {
        'Discription': 'You stand at the grand entrance of the castle. The door is open.',
        'items': ['key', 'painting', 'hammer', 'table'],
        'exits': {'north': 'Grand_Hall'},  # if we exit the entrance, we move north to Grand Hall
        'puzzel': None,
    },
    'Grand_Hall': {
        'Discription': 'A vast room with high ceilings. There is a locked door to the North.',
        'items': ['key', 'sofa', 'roundtable', 'shoes'],
        'exits': {'west': 'Entrance', 'east': 'Library', 'south': 'Basement'},
        'puzzel': 'locked door',
    },
    'Library': {
        'Discription': 'The library is filled with books. A key lies on the table.',
        'items': ['key', 'Books', 'chairs', 'candleholder'],
        'exits': {'west': 'Grand_Hall', 'south': 'Entrance'},
        'puzzel': None,
    },
    'Basement': {
        'Discription': 'A cold, dark basement. The final door is here, which is the escape door.',
        'items': ['Rusted Key', 'Old Crate', 'Broken Lantern', 'bikes', 'Cobwebs'],
        'exits': {'south': 'Entrance', 'east': 'Grand_Hall'},
        'puzzel': 'riddle',
    }
}

    
def map_game():
    for room,discrip in game_map.items():
        print(f'Room: {room}')
        print(f' Description: {discrip['Discription']}')
        print(f' Items: {discrip['items'] if discrip['items'] else 'None'}')
        print(f'  Exits:{discrip['exits']}' )
        print(f'  Puzzle: {discrip['puzzel'] if discrip['puzzel'] else 'None'}')
map_game()
