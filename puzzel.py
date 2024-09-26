from map import game_map

# List to hold solved puzzles
solved_puzzel = []

def solve_locked(current_room):
    # Get the current puzzle from the current room
    current_puzzel = game_map[current_room].get('puzzel')

    # Check if there is no puzzle
    if current_puzzel is None:
        print('There is no puzzle here.')
        return

    # If the puzzle is a locked door, solve it
    if current_puzzel == 'locked door':
        while True:
            ans = input('Enter the answer: ')
            if ans.lower() == 'key':  # Case insensitive answer check
                print('Correct! You solved the locked door puzzle.')
                solved_puzzel.append('key')
                # Mark the puzzle as solved by setting it to None
                game_map[current_room]['puzzel'] = None
                break
            else:
                print('Incorrect answer! Try again.')
    else:
        print('There is no locked puzzle here.')

# Example usage
current_room = 'Grand_Hall'  # Set the current room for testing
solve_locked(current_room)


def solve_riddle(current_room2):
    current_puzzel2=game_map[current_room2].get('puzzel',None)
    if current_puzzel2 is None:
        print('There is no puzzle here.')
        return
    
    if current_puzzel2 == 'riddle':
        while True:
            answer = input('Enter the answer: ')
            if answer.lower() == 'echo':  # Case insensitive answer check
                print('Correct! You solved the  riddle puzzle.')
                solved_puzzel.append('echo')
               
                game_map[current_room2]['puzzel'] = None
                break
            else:
                print('Incorrect answer! Try again.')
    else:
        print('There is no locked puzzle here.')
    
    
current_room2='Basement'
solve_riddle(current_room2) 
