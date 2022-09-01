import random
import csv
import math


def main_menu():
    """Upon beginning the Pokemon game, the user is prompted to choose from 5 choices on a printed out menu
       -- coded by Holden Rushing"""

    print('-----------------------  Main Menu --------------------------\n')
    menu = int(input('1 - Select a player\n2 - Select a Pokemon\n3 - Catch Pokemon\n'
                     '4 - Battle your Pokemon\n5 - End the game\n \nEnter a number 1-5: '))
    try:
        menu = int(menu)
    except TypeError:
        print("Thats a string silly!")
    if menu == 1:
        return select_player()
    if menu == 2:
        return select_pokemon()
    if menu == 3:
        return catch_pokemon()
    if menu == 4:
        return battle_pokemon_menu()
    if menu == 5:
        print('\n Thank you for playing!')
        quit()
    elif 1 <= menu >= 5:
        print('\n Please enter a number 1 through 5 only\n')
        return main_menu()


def battle_pokemon_menu():
    """This function returns the battle option that the user chose from the main menu
        -- coded by Holden Rushing"""

    menu = int(input('\n1 - Battle Pokemon\n2 - Return to the main menu\n\nPlease enter 1 or 2: '))
    if menu == 1:
        return battle_pokemon()
    if menu == 2:
        return main_menu()
    elif 1 <= menu >= 2:
        print('\n Please enter only 1 or 2\n')
        return battle_pokemon_menu()


def battle_pokemon():
    """Both players select one pokemon to battle with, players take turns
       selecting move to attack, winner is awarded 20 candy -- coded by Holden Rushing"""
    # Player 1 & 2 are selected by utilizing the "select_player()" function
    player1 = select_pokemon()
    player2 = select_pokemon()
    # player1 = ['holden', 'Pikachu', 150]
    #player2 = ['jack', 'Charizard', 150]
    # The health of the players pokemon depends on the cp level returned from the "select_player()" function
    player1_health = player1[2]
    player2_health = player2[2]
    # While both players pokemon health is greater than 0 this loops
    while player1_health > 0 and player2_health > 0:
        # A menu appears for player 1 with 3 different options
        battle_menu = int(input('\n1 - Strike (20 point damage)\n2 - Blitz (30% damage)\n'
                                '3 - Heal (10 point heal)\nPlayer 1 pick your battle option: '))
        # If user chooses option 1 they are prompted to guess a number 1-3 and if correct they deal damage
        if battle_menu == 1:
            strike = int(input('\nPick a number between 1-3. If you guess correct, your pokemon does 20 damage: '))
            number = random.randint(1, 3)
            if strike == number:
                new_p2_health = player2_health - 20
                player2_health = new_p2_health
                print('\nNice! You guessed the number and dealt 20 damage\n')
                print('Player 1\'s pokemon is at:', player1_health)
                print('Player 2\'s pokemon is at:', player2_health)
            if strike != number:
                print('\nSorry! You didn\'t guess the number so no damage was dealt\n')
                print('Player 1\'s pokemon is at:', player1_health)
                print('Player 2\'s pokemon is at:', player2_health)
        # If user chooses option 2 they are prompted to guess a number 1-4 and if correct they deal 30% damage
        if battle_menu == 2:
            blitz = int(input('\nPick a number between 1-4. If you guess correct, your pokemon does 30% damage: '))
            number = random.randint(1, 4)
            if blitz == number:
                new_p2_health = player2_health + (player2_health * -0.30)
                player2_health = new_p2_health
                print('\nNice! You guessed the number and dealt 25% damage')
                print('Player 1\'s pokemon is at:', player1_health)
                print('Player 2\'s pokemon is at:', player2_health)
            if blitz != number:
                print('\nSorry! You didn\'t guess the number so no damage was dealt')
                print('Player 1\'s pokemon is at:', player1_health)
                print('Player 2\'s pokemon is at:', player2_health)
        # If user chooses option 3 they are prompted to guess a number 1-2 and if correct their pokemon heals 10 damage
        if battle_menu == 3:
            heal = int(input('\nPick a number between 1-2. If you guess correct, your pokemon heals 10 damage: '))
            number = random.randint(1, 2)
            if heal == number:
                if player1_health <= (player1[2] - 10):
                    new_p1_health = player1_health + 10
                    player1_health = new_p1_health
                    print('Nice! You guessed the number and healed 10 damage')
                    print('Player 1\'s pokemon is at:', player1_health)
                    print('Player 2\'s pokemon is at:', player2_health)
                if player1_health > (player1[2] - 10):
                    new_p1_health = player1[2]
                    player1_health = new_p1_health
            if heal != number:
                print('\nSorry! You didn\'t guess the number so you didn\'t heal 10 damage')
                print('Player 1\'s pokemon is at:', player1_health)
                print('Player 2\'s pokemon is at:', player2_health)
        # After Player 1, A menu appears for player 2 with 3 different options
        battle_menu2 = int(input('\n1 - Strike (20 point damage)\n2 - Blitz (30% damage)\n'
                                 '3 - Heal (10 point heal)\nPlayer 2 pick your battle option: '))
        # If user chooses option 1 they are prompted to guess a number 1-3 and if correct they deal damage
        if battle_menu2 == 1:
            strike = int(input('\nPick a number between 1-3. If you guess correct, your pokemon does 20 damage: '))
            number = random.randint(1, 3)
            if strike == number:
                new_p1_health = player1_health - 20
                player1_health = new_p1_health
                print('\nNice! You guessed the number and dealt 20 damage')
                print('Player 1\'s pokemon is at:', player1_health)
                print('Player 2\'s pokemon is at:', player2_health)
            if strike != number:
                print('\nSorry! You didn\'t guess the number so no damage was dealt')
                print('Player 1\'s pokemon is at:', player1_health)
                print('Player 2\'s pokemon is at:', player2_health)
        # If user chooses option 2 they are prompted to guess a number 1-4 and if correct they deal 30% damage
        if battle_menu2 == 2:
            blitz = int(input('\nPick a number between 1-4. If you guess correct, your pokemon does 30% damage: '))
            number = random.randint(1, 4)
            if blitz == number:
                new_p1_health = player1_health + (player1_health * -0.30)
                player1_health = new_p1_health
                print('\nNice! You guessed the number and dealt 25% damage')
                print('Player 1\'s pokemon is at:', player1_health)
                print('Player 2\'s pokemon is at:', player2_health)
            if blitz != number:
                print('\nSorry! You didn\'t guess the number so no damage was dealt')
                print('Player 1\'s pokemon is at:', player1_health)
                print('Player 2\'s pokemon is at:', player2_health)
        # If user chooses option 3 they are prompted to guess a number 1-2 and if correct their pokemon heals 10 damage
        if battle_menu2 == 3:
            heal = int(input('\nPick a number between 1-2. If you guess correct, your pokemon heals 10 damage: '))
            number = random.randint(1, 2)
            if heal == number:
                if player2_health <= (player2[2] - 10):
                    new_p2_health = player2_health + 10
                    player2_health = new_p2_health
                    print('\nNice! You guessed the number and healed 10 damage')
                    print('Player 1\'s pokemon is at:', player1_health)
                    print('Player 2\'s pokemon is at:', player2_health)
                if player2_health > (player2[2] - 10):
                    new_p2_health = player2[2]
                    player2_health = new_p2_health
            if heal != number:
                print('\nSorry! You didn\'t guess the number so you didn\'t heal 10 damage')
                print('Player 1\'s pokemon is at:', player1_health)
                print('Player 2\'s pokemon is at:', player2_health)

    # Once either or both player's pokemon go below or equal to 0 there are 3 options
    # If player 1 pokemon is <= 0 but player 2 pokemon is above 0 then player 2 gets 20 candy added to their file
    if player1_health <= 0 and player2_health > 0:
        print('\nPlayer 2 wins with', player2[1] + '!\nPlayer 2 is awarded 20 candy!\n')
        file = open(player2[0], 'r')
        list = file.readlines()
        candy = int(list[0].strip())
        candy += 20
        list[0] = str(candy) + '\n'
        file.close()
        file = open(player2[0], 'w')
        file.writelines(list)
        file.close()
        return battle_pokemon_menu()
    # If player 2 pokemon is <= 0 but player 1 pokemon is above 0 then player 1 gets 20 candy added to their file
    if player2_health <= 0 and player1_health > 0:
        print('\nPlayer 1 wins with', player1[1] + '!\nPlayer 1 is awarded 20 candy!\n')
        file = open(player1[0], 'r')
        list = file.readlines()
        candy = int(list[0].strip())
        candy += 20
        list[0] = str(candy) + '\n'
        file.close()
        file = open(player1[0], 'w')
        file.writelines(list)
        file.close()
        return battle_pokemon_menu()
    # If both players pokemon are 0 or below at the end of the last round the battle ens in a draw and the
    # menu is returned
    if player1_health <= 0 and player2_health <= 0:
        print('The match ended in a draw!')
        return battle_pokemon_menu()


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
    name = input("Please enter name of player: ")
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
        candy_gain = poss_cand[random.randint(0, len(poss_cand)-1)]  # This adds candy to your candy total in the file
        file = open(name + '.txt', 'r')
        list = file.readlines()
        candy = int(list[0].strip())
        candy += candy_gain
        list[0] = str(candy) + '\n'
        file.close()
        file = open(name + '.txt', 'w')
        file.writelines(list)
        file.close()
        with open(name + '.txt', 'a') as file:
            with open('PokeList1.csv', 'r') as index:
                    limit = 1
                    for line in index:
                        limit += 1
                        if limit == num:
                            data = line.split(",")
                            data = data[1:-1]
                            data.append(1)
                            data = str(data)
                            file.write('{},{},{}\n'.format(pk_list[num], cp_l[num], '1'))
        print("You are awarded", candy_gain, " candy!")
    else:
        print("Aw, the", pokemon, "got away! Better luck time!")  # Nothing is returned if the pokemon isn't captured
    return main_menu()#The pokemon is returned to be added


# -------------------------------------------CODED BY JACK PAYNE------------------------------------------------------
def level_up(name):
    '''Csv file is opened, Player selects pokemon, chooses to give them candy,
    level up is calculated based on level and candy total is subtracted'''

    #   This takes the inputs from the user into a list, the if statements are for it to look neat and easy to understand
    pokemon_list = []
    cp_level = []
    # name = input("Please enter name of player: ")
    with open(name + '.txt', 'r') as player_file:
        count = -1
        for line in player_file:
            count += 1
            if count <= 0:
                print('Player Candies: ', line)
                print('\nPlayer Pokemons:')
            if count >= 1:
                poke, cp, level = line.split(',')
                pokemon_list.append(str(poke))
                cp_level.append(int(cp))
                print('Pokemon', count, ': ', poke, cp)
    i = int(input("Please select the pokemon you wish to level(enter a #): "))
    poke_name = pokemon_list[i-1]
    poke_index = []
    with open(name + '.txt', 'r') as file:
        poke_list = file.readlines()
        candy_total = int(poke_list[0].strip())
        for j in range(len(poke_list)):
            if poke_name in poke_list[j]:
                poke_index = line.split(',')
    poke_index[1] = int(poke_index[1])
    poke_index[2] = int(poke_index[2].strip())

    orders = 0
    while orders != 2:
        CP = poke_index[2]
        level = poke_index[1]
        print("Profile name:", name)
        print("Current Level: ", poke_index[2]) #this prints the current level and CP of chosen pokemon
        print("Current CP: ", poke_index[1])
        print("Candies: ", candy_total)
        print("1 - Use Candy to Level-Up")
        print("2 - Exit pokemon selection")
        orders = int(input(""))
        if orders == 1:             # This takes note of level differences for difference calculations and subtracts
            if poke_index[2] <= 30: # candies when used
                poke_index[2] += 1
                poke_index[1] += poke_index[1] * .0094 / (.095 * math.sqrt(poke_index[2]))
                candy_total -= 1
            elif 40 > poke_index[2] > 30:
                poke_index[2] += 1
                poke_index[1] += poke_index[1] * .0045 / (.095 * math.sqrt(poke_index[2]))
                candy_total -= 2
            elif poke_index[2] >= 40:  # This ensures the level is capped at 40 and nothing else is calculated
                poke_index[2] = 40
                print("Your Pokemon is max level.")
        elif orders == 2:
            print("Exiting pokemon selection")  # This only happens when the program ends and all loops are finished
    file = open(name + '.txt', 'r')
    list = file.readlines()
    candy = int(list[0].strip())
    candy = candy_total
    list[0] = str(candy) + '\n'
    data = list[i].split(",")
    data[1] = poke_index[2]
    data[2] = poke_index[1]
    data = str(data)[1:-1]
    list[i] = data
    file.close()
    file = open(name + '.txt', 'w')
    file.writelines(list)
    file.close()
    print(list)






def create_player():
    """This function takes in global variables, to create a players file
       and assign them their very first pokemon.
       - Coded by Leslie Ramirez"""
    name = input('Enter your name: ')
    with open(name + '.txt', 'w') as file:
        file.write('20\n')
        rand = random.randint(0, 149)
        file.write('{},{},{}\n'.format(pk_list[rand], cp_l[rand], '1'))
        global player_list
        player_list.append(name)
    return select_player()
    # file = open(name + '.txt', 'w')
    # file.write('20\n')
    # rand = random.randint(0, 149)
    # file.write('{},{},{}\n'.format(pk_list[rand], cp_l[rand], '1'))
    # global player_list
    # player_list.append(name)
    # print(player_list)
    # return select_player()


def select_player():
    """This function allows you to either create a player or select an existing player.
    - Coded by Leslie Ramirez"""
    print('PLease select a player!')
    print('Select 1, to create a new player.')
    print('Select 2, to choose an existing player.')
    print("Select 3, to exit to main menu")
    num = int(input(''))
    if num == 1:
        return create_player()
    if num == 2:
        player_name = input('Enter the players name: ')
        if player_name in player_list:
            select_pokemon()
            return main_menu()
        else:
            print('Sorry this player does not exist, please create a player.')
            return create_player()
    if num == 3:
        return main_menu()
    return main_menu()


def select_pokemon():
    """This function opens up players file, and displays number of candies and pokemons,
    then then player will have the option to choose a pokemon from their list. """
    pokemon_list = []
    cp_level = []
    name = input("Players name: ")
    while True:
        print("Select 1 - Level up pokemon")
        print("Select 2 - Set an active pokemon")
        response = int(input(""))
        try:
            response = int(response)
        except TypeError:
            print("Thats a string silly!")
        if response == 1:
            level_up(name)
        else:
            break
    with open(name + '.txt', 'r') as player_file:
        count = -1
        for line in player_file:
            count += 1
            if count <= 0:
                print('Player Candies: ', line)
                print('\nPlayer Pokemons:')
            if count >= 1:
                poke, cp, level = line.split(',')
                pokemon_list.append(str(poke))
                cp_level.append(int(cp))
                print('Pokemon #', count, ':Name', poke, ' CP -', level, "  ", "Level -", cp)
    p = int(input('Select active pokemon.(enter Pokemon #): ')) - 1
    return [name, pokemon_list[p], cp_level[p]]


pk_list = []
cp_l = []
cp2_l = []
player_list = []
with open('PokeList1.csv') as pokemon:
    pokes = csv.reader(pokemon, delimiter=',')
    list = []
    for row in pokes:
        list.append(row)
    del list[0]
    for i in range(len(list)):
        pk_list.append(list[i][1])
        cp_l.append(list[i][2])
        cp2_l.append(list[i][3])


main_menu()
