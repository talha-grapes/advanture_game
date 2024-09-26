from map import game_map
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
        elif direction_input.startswith('go'):
            direction_input = direction_input[3:]                  
            if direction_input in room['exits']:
                next_room=room['exits'][direction_input]
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
                if 1 <= item_choice <= len(items):
                    picked_item=items.pop(item_choice-1)
                    player['inventory'].append(picked_item)
                    print(f'You have taken: {picked_item}')
                else:
                    ('Invalid choice')
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
                    if 1 <= item_choice <= len(items):
                        dropped_item = player['inventory'].pop(item_choice - 1)
                        
                        room['items'].append(dropped_item)  # Add dropped item back to the room
                        player['Dropped_inventory'].append(dropped_item) 
                        print(f'You have dropped: {dropped_item}')
                    else:
                        print('invalid choice')
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
while True:
    command = input('Enter a command ("inventory", "exit","direction"): ').lower()
    
    if command == 'inventory':
        show_inventory()  # Call function to manage inventory (take/drop items)
    elif command == 'exit':
        print("Exiting the game.")
        break
    elif command == 'direction':
        direction()
       
            # Call direction function to navigate the map
    else:
        print("Invalid command. Try 'inventory' or 'exit'or 'direction.")