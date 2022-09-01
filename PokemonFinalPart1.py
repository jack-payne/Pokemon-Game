
def main_menu():
    '''Upon beginning the game, the user is prompted to choose from 5 choices on a printed out menu:
    1.Selecting a player,  2. Selecting a pokemon, 3. Catching pokemon, 4. Battling between pokemon, 5. Ending the game'''
    pass


def select_pokemon():
    '''Once a player is selected, a file is called with the players list of pokemons with their current CP,
     and stored candies. If a new pokemon is catched, it is added to the players file. This will return the pokemon chosen by the player. '''
    pass


def select_player():
    '''Option to choose a previous player or to create a new players account,
     then returns players list of pokemons'''
    pass


def catch_pokemon():
    '''Opens csv file, Selects pokemon to catch and play game, if game True then pokemon is caught,
     adds pokemon name to csv file, takes input for name of desired pokemon'''
    pass


def battle_pokemon():
    '''Opens csv file, Both players select one pokemon to battle with,
     players take turns selecting move to attack, winner is awarded 20 candy'''
    pass


def level_up():
    '''Csv file is opened, Player selects pokemon, chooses to give them candy,
    level up is calculated based on level and candy total is subtracted'''
    pass
  # ---------------------------------MAIN CODE -----------------------------------------
# Player opens main menu, the options are to 1.sign in, 2. select pokemon, 3. catch new pokemon, 4. level
# up a chosen pokemon with candy, 5.Battle a friend, and 6. Exit Game
# Selecting one to five with open up the corresponding function with the users account information
# If they exit the game the program will stop running

# If any option other than sign in it selected when two players are not signed in a message will pop up
# informing the user that they need to sign in to do this.

# All submenus will have the ability to go back to main menu but their current task data will be lost

# The main code really just consists of opening the main menu because that makes it easier to reopen
# it if we call it in a function

# Print statement that says "Thank you for playing!"
