import re
from secrets import choice
import time
import threading
import json

time_up = False

def display_title():
    print(" #############################################")
    print(" #                                           #")
    print(" #            Welcome to the Game!           #")
    print(" #                  ESCAPIST!                #")
    print(" #                                           #")
    print(" #############################################") 
    
def get_username():
    username = input("Please enter your username: ")
    pattern = r"^[A-Za-z0-9_]{5,15}$"

    if re.fullmatch(pattern, username):
        print("Welcome, " + username + "!")
    else:
        print("Invalid username.")
        print("Username must be 5-15 characters.")
        print("Only letters, numbers, and underscores are allowed.")
        get_username()  # Prompt the user again if the username is invalid
    return username
        
def save_player(username, result):
    
    # try:
    #     with open("players.json", "r") as file:
    #         players = json.load(file)

    # except FileNotFoundError:
    #     players = []
        
    player = {
        "username": username,
        "result": result
    }
    
    # players.append(player)

    with open("players.json", "w") as file:
        json.dump(player, file, indent=4)

    print("Player data saved!")
    

def play_game():
    choice = input("view clue? (y/n): ")
    if choice.lower() == "y":
        print("\nYou have 30 seconds to solve the clue!")
        print("God made the whole numbers, all else is the work of man.")
        print("###########################################################")
        print("##      WHITE: 15/4      BLACK: 18/8      RED: 72/8      ##")
        print("###########################################################")
        
        
        print("\nYou have 30 seconds to choose a door.")
        print("White? Black? Red?")
    
        # Start timer
        timer_thread = threading.Thread(target=timer)
        timer_thread.daemon = True
        timer_thread.start()
    
        # ask while timer is running
        choice = input("Which door do you choose? (white/black/red): ").lower()
    
        # time to solve and pick a door
        if not time_up:
            if choice == "red":
                print("You chose the red door. You escaped!")
                result = "escaped"
            elif choice == "black":
                print("You chose the black door. You stepped into a very dark place and fell to your death!")
                result = "fell to death"
            elif choice == "white":
                print("You chose the white door. You are blinded, getting lost in your path till you died!")
                result = "died"
            else:
                print("Invalid choice. Please choose 'red', 'black', or 'white'.")
                
            return result
        else:
            print("You failed to pick a door in time. Game over!")
    else:
        print("You chose not to view the clue. You cannot proceed without it.")
                
        
def play_again():
    choice = input("Play again? (y/n): ")

    if choice.lower() == "y":
        return True
    else:
        return False

        
def timer():
    global time_up
    
    print("\nCountdown timer started! You have 30 seconds to choose a door.")
    
    for seconds in range(30, 0, -1):
        # print(f"\nTime remaining: {seconds} seconds")
        
        
        if choice == "white" or choice == "red" or choice == "black":
            print("You picked door", choice)
            break
        
        time.sleep(1)
        
    time_up = True
    print("\nTime's up! You failed to pick a door in time. Game over!")
    
    
           

    
def main():
    display_title()
    username = get_username()   
    
    print("\nYou woke up in a mysterious room.")
    print("You need to find a way to escape.")
    print("There are three doors in front of you.")
    print("One door is red, one is black, and one is white.")
    print("Choose wisely, as each door leads to a different outcome.")
    
    print("\nAs you roam around the room, you find a clue written on the wall.")
    print("The clue reads: 'God made the whole numnbers, all else is the work of man.'")
    print("below is a set of math problems that you need to solve \nto figure out the right door based on the quote above.")
    print("\nYou have 30 seconds to solve the problem and pick a door.")
    print("If you don't choose in time, you will lose the game.")
    print("Good luck!")
    
    while True:
        result = play_game()

        if play_again() == False:
            print("Thanks for playing!")
            break
        
    
    save_player(username, result)
        
main()
