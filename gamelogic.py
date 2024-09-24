from map import game_map
current_room='Entrance'

def direction():
    global current_room
    while True:
        room = game_map[current_room] 
         
    
        if room==current_room:
           print(f'Description of {current_room}: {room["Discription"]}')
        direction_input=input('enter thr direction: ' )
        if direction_input=='look':
                print(f'Description of {current_room}: {room["Discription"]}')
                continue 
                 
        if direction_input  not in room['exits']:
            print('Exit the game.GoodBye!')
            break
                             
        if direction_input in room['exits']:
                    next_room=room['exits'][direction_input]
                    current_room=next_room
                    print(f'Description of {current_room}: {room["Discription"]}')
        else:
            print('invalid direction!')
                
                


direction()
                
            
            
                
            
    
                 