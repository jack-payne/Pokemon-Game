
import csv
import random
import math
import PokemonOtherFunctions as other
# -------------------------------------------CODED BY JACK PAYNE------------------------------------------------------
def game():
    '''Plays hangman to determine if player captures pokemon, returns True if player wins and False if player loses'''
    word_pool = 'engineering pokemon digimon yugioh python class game pikachu coding'.split()
    word = word_pool[random.randint(0, len(word_pool) - 1)]
    guesses = ''
    turns = 10
    while turns > 0: # This gives the player 10 tries for incorrect letters
        failed = 0
        for char in word:
            if char in guesses: # This for loop prints out blank lines for undiscovered letters and
                print(char)     # prints out the letters if guess correctly in their placement
            else:
                print("_")
                failed += 1
        if failed == 0: #  if no blank lines are printed, you win
            print("You won")
            break
        guess = input("Guess a letter: ")  # This keeps track of your attempts
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong")
        print("You have", + turns, 'more guesses')  # This just tells you how many guesses you have left
        if turns == 0:
            print("You Lose")
            return False # False if you lose
    return True  # True if you win
# -------------------------------------------CODED BY JACK PAYNE------------------------------------------------------
def catch_pokemon():
    '''Opens csv file, Selects pokemon to catch and play game, if game True then pokemon is caught,
     adds pokemon name from csv file,returns name of captured pokemon or returns nothing if pokemon wasn't captures'''
    name = other.select_player()
    with open('PokeList1.csv', 'r') as index:
        num = random.randint(2, 151) #This generates a random polemon drawn from the csv file
        limit = 1

        for line in index:
            limit += 1
            data = line.split(',')
            if limit == num:
                pokemon = data[1]
    if pokemon[0].lower() == 'a' or pokemon.lower()[0] == 'e' or  pokemon.lower()[0] == 'i' or pokemon.lower()[0] == 'o' or pokemon.lower()[0] == 'u':
        print("Wow! You found an", pokemon, "\b!")
    else:                                             # This is just for grammatical accuracy(a and an)
        print("Wow! You found a", pokemon, "\b!")
    print("To catch the", pokemon, "you're going to need to win a game of hangman!")
    answer = input('Are you ready?(yes or no): ')
    if answer == 'yes': # This runs the game() function
        print('Have fun!')
        result = game()
    else:
        print('Well to bad, have fun!') # This is just for fun
        result = game()
    poss_cand = [1, 3, 5, 10]
    if result == True: # If you win the game, the pokemon is returned from the function to be added to the players index
        print('congratulations! You have added the', pokemon, 'to your collection!')
        candy_gain = poss_cand[random.randint(0, len(poss_cand))]  # This adds candy to your candy total in the file

        file = open(name, 'r')
        list = file.readlines()
        candy = int(list[0].strip())
        candy += candy_gain
        list[0] = str(candy) + '\n'
        file.close()
        file = open(name, 'w')
        file.writelines(list)
        file.close()

        print("You are awarded", candy_gain, "!")
        return pokemon #The pokemon is returned to be added
    else:
        print("Aw, the", pokemon, "got away! Better luck time!") # Nothing is returned if the pokemon isn't captured

# -------------------------------------------CODED BY JACK PAYNE------------------------------------------------------
def level_up():
    '''Csv file is opened, Player selects pokemon, chooses to give them candy,
    level up is calculated based on level and candy total is subtracted'''
    Poke = []
    #   This takes the inputs from the user into a list, the if statements are for it to look neat and easy to understand
    # for i in range(4):
    #     if i == 0:
    name = input("Please enter name of player: ")
    poke_name = input("Please enter name of pokemon you wish to level up")
    poke_index = []
    with open(name, 'r') as file:
        poke_list = file.readlines()
        candy_total = int(poke_list[0].strip())
        for line in poke_list:
            if poke_name in poke_list:
                poke_index = line.split(',')
    poke_index[1] = int(poke_index[1])
    poke_index[2] = int(poke_index[2].strip())
    print(poke_index)
    orders = 0
    while orders != 2:
        CP = poke_index[2]
        level = poke_index[1]
        print(name)
        print("Current Level: ", poke_index[2]) #this prints the current level and CP of chosen pokemon
        print("Current CP: ", poke_index[1])
        print("Candies: ", candy_total)
        print("1 - Use Candy to Level-Up")
        print("2 - Exit to Main Menu")
        orders = int(input(""))
        if orders == 1:             # This takes note of level differences for difference calculations and subtracts
            if poke_index[2] <= 30: # candies when used
                poke_index[2] += 1
                poke_index[1] += poke_index[1] * .0094 / math.pow(.095 * math.sqrt(poke_index[2]), 2)
                candy_total -= 1
            elif 40 > poke_index[2] > 30:
                poke_index[2] += 1
                poke_index[1] += poke_index[1] * .0045 / math.pow(.095 * math.sqrt(poke_index[2]), 2)
                candy_total -= 2
            elif poke_index[2] >= 40:  # This ensures the level is capped at 40 and nothing else is calculated
                poke_index[2] = 40
                print("Your Pokemon is max level.")
        elif orders == 2:
            print("Exiting to Main Menu")  # This only happens when the program ends and all loops are finished
    return CP, level
list = [1,2 ,3, 4]
print(list[-1:])


# file = open(player2[0], 'r')
#         list = file.readlines()
#         candy = int(list[0].strip())
#         candy += 20
#         list[0] = str(candy) + '\n'
#         file.close()
#         file = open(player2[0], 'w')
#         file.writelines(list)
#         file.close()

