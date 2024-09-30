from map import game_map
import puzzel

import json

current_room='Entrance'

def direction():
    global current_room
    
    while True:
        room = game_map[current_room] 
        print(f'Description of {current_room}: {room["Discription"]}')
        direction_input=input('enter the direction (e.g:go north) ): ' )
        if direction_input=='look':
            print(f'Description of {current_room}: {room["Discription"]}')
        elif direction_input =='exit':
            print('Exit the game.GoodBye!')
            break
        if direction_input=='examine':
            puzzel.examine()
        elif direction_input.startswith('go'):
            direction_input = direction_input[3:]                  
            if direction_input in room['exits']:
                next_room=room['exits'][direction_input]
                puzzel_solved=False
                
                print('solve the puzzel then move')
                if game_map[next_room].get('puzzel'):
                    if game_map[next_room]['puzzel']=='locked door':
                        print(f'the door to {next_room} is locked . Solve the Puzzel')
                        puzzel_solved=puzzel.solve_locked(next_room,player)
                    if game_map[next_room]['puzzel']=='riddle':
                         print(f'the door to {next_room} is locked . Solve the Puzzel')
                         puzzel_solved=puzzel.solve_riddle(next_room,player)
                        
                if puzzel_solved:
                    current_room=next_room
                    print(f'You have moved to: {current_room}')
                    print(f'Description of {current_room}: {room["Discription"]}')
                    player['score']+=10
                    print(f'player score is {player["score"]}')
                
             # Ask if the player wants to manage inventory after movement
                manage_inventory = input("Do you want to manage your inventory? (yes/no): ").lower()
                if manage_inventory == 'yes':
                    inventory_player()
                else:
                    print('invalid direction!')
        else:
            print('invalid comand')
        
    show_inventory() 
    
           
    
  
  
  
  
player={
    'name': 'Player ',   
    'inventory': [],           
    'score': 0,
    'Dropped_inventory':[],
    
  }              


def inventory_player():
    global current_room
    room = game_map[current_room]  # Get the current room from the game map
    items = room.get('items',[])
    action_choice = input('Do you want to "take" or "drop" an item? ')
    if action_choice=='take':
        if not items:
            print('There are no items in the room')
            return
        
        print('items in the room')
        
        for i,item in enumerate(items,start=1):
            print('index of the item',i,'item name',item)
        while True:
            try:
        
                item_choice = int(input("Enter the number of the item you want to take : "))
                if item_choice==0 or item_choice>len(items):
                    print('You chose to stop taking items.')
                    break
                picked_item=items.pop(item_choice-1)
                player['inventory'].append(picked_item)
                print(f'You have taken: {picked_item}')
            except ValueError:
                    print("Please enter a valid number.")
    elif action_choice=='drop':
            if not player['inventory']:
                print(" No items in our inventory to drop.")
                return
            
            print('Our inventory')
            for i, item in enumerate(player['inventory'],start=1):
                print(f'{i}. {item}')
            while True:
                try:
            
                    item_choice=int(input('enter the number of item you want to drop: '))
                    if  item_choice==0 or item_choice>len(player['inventory']):
                        print('You chose to stop dropping items.')
                        break
                    
                    dropped_item = player['inventory'].pop(item_choice - 1)
                        
                    room['items'].append(dropped_item)  # Add dropped item back to the room
                    player['Dropped_inventory'].append(dropped_item) 
                    print(f'You have dropped: {dropped_item}')
            
                except ValueError:
                    print("Please enter a valid number.") 
    else:
        print('invalid action! Please choose take or drop')      
def show_inventory():
    """Display the player's current inventory items."""
    if not player['inventory']:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i, item in enumerate(player['inventory'], start=1):
            print(f'{i}. {item}')
            
            
def save_game(filename='savefile.json'):
    game_state = {
        'current_room': current_room,
        'inventory': player['inventory'],
        'score': player['score'],
    }
    try:
        with open(filename, 'w') as file:
            json.dump(game_state, file)
        print(f'Game saved successfully to {filename}.')
    except Exception as e:
        print(f"An error occurred while saving the game: {e}")
        
        

def load_game(filename='savefile.json'):
    global current_room, player
    
    try:
        with open(filename, 'r') as file:
            game_state = json.load(file)
            current_room = game_state['current_room']
            player['inventory'] = game_state['inventory']
            player['score'] = game_state['score']
        print(f'Game loaded successfully from {filename}.')
        print(f'You are currently in {current_room}.')
    except FileNotFoundError:
        print(f'No save file found with the name {filename}. Start a new game or try a different file.')
    except Exception as e:
        print(f"An error occurred while loading the game: {e}")


            
            


while True:
    command = input('Enter a command ("inventory", "exit","direction","examine","save","load"): ').lower()
    
    if command == 'inventory':
        show_inventory()  # Call function to manage inventory (take/drop items)
    elif command == 'exit':
        print("Exiting the game.")
        break
    elif command == 'direction':
        direction()
    elif command=='examine':
        puzzel.examine()
    elif command=='save':
        save_game()
    elif command=='load':
        load_game()
        
    
       
    else:
        print("Invalid command. Try 'inventory' or 'exit'or 'direction.")