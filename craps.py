# Title: Craps
# Author: Benjamin Lemery
# Date: 10/24/19
# This program allows the user to play a virtual game of craps.
import random
random.seed()

bankroll = int(input("How much money are you playing with? (Enter a dollar amount): "))

# Setups the game to begin
def create():
    menu_selection = int(input("Are you ready to begin a game of Craps? \nPress 1 to play.\nPress 2 to quit."))
    if menu_selection == 1:
        print("You have this much money in your bank account: $" + str(bankroll))
        money_to_bet = int(input("How much money would you like to bet this round?: "))
        check_bankroll(money_to_bet)
    else:
        exit_game()


# Checks the users bank account to verify that there is enough money for them to keep playing.
def check_bankroll(money_to_bet):
    global bankroll
    if bankroll >= money_to_bet:
        play_game(money_to_bet)
    elif bankroll == 0:
        print("You lost.")
        exit_game()
    elif bankroll < money_to_bet:
        print("You don't have enough money to bet that much. Try again.")
        create()


def play_game_again():
    global bankroll
    # Determins what happens when the user runs out of money.
    if bankroll == 0:
        print("You ran out of money.")
        start_over = int(input("Would you like to start over? (Press 1 to start over or 2 to exit the game."))
        if start_over == 1:
            bankroll = int(input("How much money are you playing with? (Enter a dollar amount): "))
            create()
        elif start_over == 2:
            exit_game()
    else:
        play_again = int(input(
            "Would you like to play another round of Craps or are you ready to call it quits? (Enter 1 to play again or 2 to exit.)"))
        if play_again == 1:
            create()
        elif play_again == 2:
            exit_game()


def exit_game():
    print("\nExiting the game..")
    exit()


def play_game(money_to_bet):
    global bankroll
    sum_of_dice = roll_dice()
    # Checks if the user immediately won.
    if sum_of_dice == 7 or sum_of_dice == 11:
        print("You rolled a " + str(sum_of_dice) + " You win!")
        bankroll += money_to_bet
        print("You have this much money in your bank account. $" + str(bankroll))
        play_game_again()
        # Checks if the user immediately lost.
    elif sum_of_dice == 2 or sum_of_dice == 3 or sum_of_dice == 12:
        print("You rolled a " + str(sum_of_dice) + " You lost!")
        bankroll -= money_to_bet
        print("You have this much money in your bank account: $" + str(bankroll))
        play_game_again()
        # Allows the user to continue playing until they roll their first value again and they win or until they role a 7 and lose.
    else:
        print("You rolled a " + str(sum_of_dice))
        desired_value = sum_of_dice
        while sum_of_dice != 7 or sum_of_dice != desired_value:
            sum_of_dice = roll_dice()
            print("You a rolled a: " + str(sum_of_dice))
            if sum_of_dice == 7:
                print("You lost the game!")
                bankroll -= money_to_bet
                play_game_again()
            elif sum_of_dice == desired_value:
                print("You won the game!")
                bankroll += money_to_bet
                play_game_again()

# Generates a list of the dice values and adds up the values to get the sum.
def roll_dice():
    print("\nRolling the dice..")
    dice = ['', '']
    dice[0] = random.randrange(1, 6)
    dice[1] = random.randrange(1, 6)
    return (sum(dice))


create()
