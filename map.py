# Make map that represent rooms,exits,items,puzzels and discription
# we used dictionary to nake the map
game_map={
    'Entrance':{
    'Discription':'Stand the grand Entrance of the castle. The door is open',
    'items':['key','painting','hammer','table'],
    'exits':{'north':'Grand_Hall'},#if we exit the entrance the move north to ground hall
    'puzzel':None,
 
    
    },
    'Grand_Hall':{
        'Discription':'A vast room with high ceilings and space.There is a locked door to the North',
        'items':['key','sofa','roundtable','shoes'],
        'exits':{'west':'Entrance','east':'Library','south':'Basement'},
        'puzzel':'locked door',
       
    },
    'Library':{
        'Discription':'library is filled with books. A key lies on the table',
        'items':['key','Books','chairs','candleholder'] ,#we set key in default
        'exits':{'west:''Grand_hall','south:' 'Entrance'},
        'puzzel':None,
        
    },
    'Basement':{
        'Discription':'A cold dark basement . Final door .Also this is escape door',
        'items':['Rusted Key', 'Old Crate', 'Broken Lantern', 'bikes', 'Cobwebs'],
        'exits':{'south': 'Entrance','east':'Entrance'},
        'puzzel':'riddle',
        
        
        
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
