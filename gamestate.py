import json

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
