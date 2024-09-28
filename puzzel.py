from map import game_map

# List to hold solved puzzles
solved_puzzel = []

def solve_locked(current_room):
    current_puzzel = game_map[current_room].get('puzzel')

    if current_puzzel is None:
        print('There is no puzzle here.')
        return False

    if current_puzzel == 'locked door':
        while True:
            answer = input('Enter the answer (type "exit" to give up): ')
            if answer.lower() == 'exit':
                print("You chose to give up on this puzzle.")
                return False
            elif answer.lower() == 'key':
                print('Correct! You solved the locked door puzzle.')
                solved_puzzel.append('key')
                game_map[current_room]['puzzel'] = None  # Mark as solved
                return True
            else:
                print('Incorrect answer! Try again.')
    else:
        print('There is no locked puzzle here.')
        return False


def solve_riddle(current_room):
    current_puzzel = game_map[current_room].get('puzzel', None)
    
    if current_puzzel is None:
        print('There is no puzzle here.')
        return False
    
    if current_puzzel == 'riddle':
        while True:
            answer = input('Enter the answer (type "exit" to give up): ')
            if answer.lower() == 'exit':
                print("You chose to give up on this puzzle.")
                return False
            elif answer.lower() == 'echo':
                print('Correct! You solved the riddle puzzle.')
                solved_puzzel.append('echo')
                game_map[current_room]['puzzel'] = None  # Mark as solved
                return True
            else:
                print('Incorrect answer! Try again.')
    else:
        print('There is no riddle puzzle here.')
        return False


def examine():
    """Function to examine an object in the room."""
    print('What would you like to examine? ')  # Adjust based on your room's items
    choice = input("Enter your choice: ").strip().lower()
    if choice == 'table':
        print("The table is covered with dust and a key is hidden beneath it.")
        return 'key'  # This could be an item you add to the player's inventory
    elif choice == 'sofa':
        print("You find some old coins and a note that reads, 'The answer is everywhere.'")
    elif choice == 'books':
        print("You find a book titled 'The Secrets of the Castle'. It looks intriguing.")
    else:
        print("You don't see that here.")
