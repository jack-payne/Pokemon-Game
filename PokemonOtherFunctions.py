# ---------------------------------LESIE CODE--------------------------------------
import csv
import random
import PokemonFinalPart1 as other
def create_player():
    """This function takes in global variables, to create a players file
       and assign them their very first pokemon.
       - Coded by Leslie Ramirez"""
    name = input('Enter your name: ')
    file = open(name, 'w')
    file.write('20\n')
    rand = random.randint(0, 149)
    file.write('{},{},{}\n'.format(pk_list[rand], cp_l[rand],'1'))
    global player_list
    player_list.append(name)


def select_player():
    """This function allows you to either create a player or select an existing player.
    - Coded by Leslie Ramirez"""
    print('PLease select a player!')
    print('Select 1, to create a new player.')
    print('Select 2, to choose an existing player.')
    num = int(input(''))
    if num == 1:
        return create_player()
    if num == 2:
        player_name = input('Enter the players name: ')
        if player_name in player_list:
            return select_pokemon()
        else:
            print('Sorry this player does not exist, please create a player.')
            return create_player()
pass


def select_pokemon():
    """This function opens up players file, and displays number of candies and pokemons,
    then then player will have the option to choose a pokemon from their list. """
    name = input('Players name: ')
    pokemon_list = []
    cp_level = []
    with open(name, 'r') as player_file:
        count = -1
        for line in player_file:
            count += 1
            if count <= 0:
                print('Player Candies: ', line)
                print('\nPlayer Pokemons:')
            if count >= 1:
                poke, cp = line.split(',')
                pokemon_list.append([poke])
                cp_level.append([cp])
                print('Pokemon', count, ': ', poke, cp)

    p = int(input('Which pokemon would you like to choose (enter a #): ')) - 1
    print(pokemon_list[p], cp_level[p])
    return pokemon_list[p], cp_level[p]
pk_list = []
cp_l = []
cp2_l = []
player_list = ['Leslie']
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

# ----------------------------HOLDEN RUSHING-------------------
import random

def main_menu():
    """Upon beginning the Pokemon game, the user is prompted to choose from 5 choices on a printed out menu"""

    print('-----------------------  Main Menu --------------------------\n')
    menu = int(input('1 - Select a different player\n2 - Select a Pokemon\n3 - Catch Pokemon\n'
                     '4 - Battle your Pokemon\n5 - End the game\n \nEnter a number 1-5: '))
    if menu == 1:
        return select_player()
    if menu == 2:
        return select_pokemon()
    if menu == 3:
        return other.catch_pokemon()
    if menu == 4:
        return battle_pokemon_menu()
    if menu == 5:
        print('\n Thank you for playing!')
        quit()
    elif 1 <= menu >= 5:
        print('\n Please enter a number 1 through 5 only\n')
        return main_menu()


def battle_pokemon_menu():
    """This function returns the option that the user chose from the battle pokemon menu"""

    menu = int(input('\n 1 - Battle Pokemon\n 2 - Return to the main menu'))
    if menu == 1:
        return battle_pokemon()
    if menu == 2:
        return main_menu()
    elif 1 <= menu >= 2:
        print('\n Please enter only 1 or 2\n')
        return battle_pokemon_menu()


def battle_pokemon():
    """Opens csv file, Both players select one pokemon to battle with,
       players take turns selecting move to attack, winner is awarded 20 candy"""

    player1 = ['pikachu', 100]
    player2 = ['charizard', 100]

    player1_health = player1[1]
    player2_health = player2[1]

    while player1[1] > 0 and player2[1] > 0:
        battle_menu = int(input('\n1 - Strike (20 point damage)\n2 - Blitz (30% damage)\n'
                                '3 - Heal (10 point heal)\nPlayer 1 pick your battle option: '))
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
        if battle_menu == 3:
            blitz = int(input('\nPick a number between 1-2. If you guess correct, your pokemon heals 10 damage: '))
            number = random.randint(1, 2)
            if blitz == number:
                if player1_health <= (player1[1] - 10):
                    new_p1_health = player1_health + 10
                    player1_health = new_p1_health
                    print('Nice! You guessed the number and healed 10 damage')
                    print('Player 1\'s pokemon is at:', player1_health)
                    print('Player 2\'s pokemon is at:', player2_health)
                if player1_health > (player1[1] - 10):
                    new_p1_health = player1[1]
                    player1_health = new_p1_health
            if blitz != number:
                print('\nSorry! You didn\'t guess the number so you didn\'t heal 10 damage')
                print('Player 1\'s pokemon is at:', player1_health)
                print('Player 2\'s pokemon is at:', player2_health)

        battle_menu2 = int(input('\n1 - Strike (20 point damage)\n2 - Blitz (30% damage)\n'
                                 '3 - Heal (10 point heal)\nPlayer 1 pick your battle option: '))
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
        if battle_menu2 == 3:
            heal = int(input('\nPick a number between 1-2. If you guess correct, your pokemon heals 10 damage: '))
            number = random.randint(1, 2)
            if heal == number:
                if player2_health <= (player2[1] - 10):
                    new_p2_health = player2_health + 10
                    player2_health = new_p2_health
                    print('\nNice! You guessed the number and healed 10 damage')
                    print('Player 1\'s pokemon is at:', player1_health)
                    print('Player 2\'s pokemon is at:', player2_health)
                if player2_health > (player2[1] - 10):
                    new_p2_health = player2[1]
                    player2_health = new_p2_health
            if heal != number:
                print('\nSorry! You didn\'t guess the number so you didn\'t heal 10 damage')
                print('Player 1\'s pokemon is at:', player1_health)
                print('Player 2\'s pokemon is at:', player2_health)

    if player1_health <= 0 and player2_health > 0:
        print('\nPlayer 2 wins with', player2[0] + '!\nPlayer 2 is awarded 20 candy!\n')
        player_candy[0] += 20
        return battle_pokemon_menu()
    if player2_health <= 0 and player1_health > 0:
        print('\nPlayer 1 wins with', player1[0] + '!\nPlayer 1 is awarded 20 candy!\n')
        player_candy[1] += 20
        return battle_pokemon_menu()
    if player1_health <= 0 and player2_health <= 0:
        print('The match ended in a draw!')
        return battle_pokemon_menu()

