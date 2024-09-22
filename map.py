# Make map that represent rooms,exits,items,puzzels and discription
# we used dictionary to nake the map
game_map={
    'Entrance':{
    'Discription':'Stand the grand Entrance of the castle. The door is open',
    'items':[],
    'exits':{'north':'grandhall'},#if we exit the entrance the move north to ground hall
    'puzzel':None,
    'Score':[0]
    
    },
    'Grand_Hall':{
        'Discription':'A vast room with high ceilings and space.There is a locked door to the North',
        'items':[],
        'exits':{'west':'Entrance','east':'Library','south':'basement'},
        'puzzel':'Find a key. The door is locked on north side',
        'Score':[]
    },
    'Library':{
        'Discription':'library is filled with books. A key lies on the table',
        'items':['key'] ,#we set key in default
        'exits':{'west:''Grand_hall'},
        'puzzel':None,
        'Score':[]
    },
    'Basement':{
        'Discription':'A cold dark basement . Final door .Also this is escape door',
        'items':[],
        'exits':{'south': 'Entrance'},
        'puzzel':'solve the puzzel to unlock the escape door',
        'Score':[]
        
        
    }
    
}
#player starts with  entrance
player={
    'current_room':['entrance'],
    'Inventory':[]
}
    
def map_game():
    for room,discrip in game_map.items():
        print(f'Room: {room}')
        print(f' Description: {discrip['Discription']}')
        print(f' Items: {discrip['items'] if discrip['items'] else 'None'}')
        print(f'  Exits:{discrip['exits']}' )
        print(f'  Puzzle: {discrip['puzzel'] if discrip['puzzel'] else 'None'}')
        print(f'  Score: {discrip['Score']}')
    

map_game()
