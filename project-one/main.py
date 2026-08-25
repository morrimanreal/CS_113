import re

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
        print("Make sure to escape!")
    else:
        print("Invalid username.")
        print("Username must be 5-15 characters.")
        print("Only letters, numbers, and underscores are allowed.")
        get_username()  # Prompt the user again if the username is invalid
        
display_title()
get_username()