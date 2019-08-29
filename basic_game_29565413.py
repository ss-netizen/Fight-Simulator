"""
WRITTEN BY - SHIVAM PRATAP SINGH
STUDENT ID - 29565413
VERSION - PYTHON 3
START DATE - 11-08-2018
LAST UPDATE - 23-08-2018

This is a basic python program that simulates the battle between two armies. It is a 2 user game wherein
each user is given an initial amount of $10 to buy their own armies that consists of Archers, Soldiers and Knights.
After both the armies are complete, it simulates the battle and then shows the final result. The result of each
combat is decided based on the outcome table. After one of the armies is finished/dead, the Player whose army is
still alive is declared the winner of the Battle.
"""

global flag
flag = 0

"""
This is the menu() function, it shows the units available for the players to select.
"""


def menu():
    print("\nUnits available for purchase :\n")
    print("1. Archer (Price : $1)")
    print("2. Soldier (Price : $1)")
    print("3. Knight (Price : $1)")
    print("4. Exit\n")


# Taking input from Player 1

# The initial amount for the player to begin with is assigned as $10
funds_user1 = 10
army_user1 = []
menu()
print("Player 1 : \nEnter which unit you want to buy by pressing 1,2 or 3 (Press 4 for exit) :")

# The while loop keeps running until all funds are finished.
while funds_user1 > 0:
    print('Funds available = $', funds_user1)
    user1_input = input('Enter your choice:')

# Adds the unit to the army based on the player's selection and then decrements the fund by $1 for every unit bought
    if user1_input == '1':
        army_user1.append('Archer')
        funds_user1 -= 1
    if user1_input == '2':
        army_user1.append('Soldier')
        funds_user1 -= 1
    if user1_input == '3':
        army_user1.append('Knight')
        funds_user1 -= 1
    if user1_input == '4':
        break
    if user1_input != '1' and user1_input != '2' and user1_input != '3' and user1_input != '4':
        print('Enter correct input')
        menu()

    print('Player 1 Army :', army_user1)
print('\nPlayer 1 Final Army :', army_user1)

# Taking input from Player 2

# The initial amount for the player to begin with is assigned as $10
menu()
funds_user2 = 10
army_user2 = []
print("Player 2 : \nEnter which unit you want to buy by pressing 1,2 or 3 (Press 4 for exit) :")

while funds_user2 > 0:
    print('Funds available = $', funds_user2)
    user2_input = input('Enter your choice:')

    if user2_input == '1':
        army_user2.append('Archer')
        funds_user2 -= 1
    if user2_input == '2':
        army_user2.append('Soldier')
        funds_user2 -= 1
    if user2_input == '3':
        army_user2.append('Knight')
        funds_user2 -= 1
    if user2_input == '4':
        break
    if user2_input != '1' and user2_input != '2' and user2_input != '3' and user2_input != '4':
        print('Enter correct input')
        menu()

    print('Player 2 Army :', army_user2)
print('\nPlayer 2 Final Army :', army_user2)

"""
The print_army function prints the army for both Players until all their units are finished/dead.
"""


def print_army():
    if len(army_user1) != 0:
        print('\nPlayer 1 Army:', army_user1)
    if len(army_user2) != 0:
        print('Player 2 Army:', army_user2)


"""
winner() function shows the final winner of the battle, here the conditions mentioned are: If Army of Player 1 
is finished but still there are units left in Player 2 Army then Player 2 is the winner and vice versa for Player 1.
If both of the armies are empty, the battle ends in a tie.
The flag variable turns 1 if there is a winner.
"""


def winner():
    if len(army_user1) != 0 and len(army_user2) == 0:  # All units in Player 2 army are finished
        print('Player 2 Army:', army_user2)
        print('Player 1 Wins the Battle')
        global flag
        flag = 1
    elif len(army_user2) != 0 and len(army_user1) == 0:  # All units in Player 1 army are finished
        print('\nPlayer 1 Army:', army_user1)
        print('Player 2 Wins the Battle')
        flag = 1
    elif len(army_user1) == 0 and len(army_user2) == 0:  # All units in both armies are finished
        print(".....Both the armies are dead, Battle ends in a Tie.....")
        flag = 1

# Combat begins
print('\n')
print('******.....The Battle Begins.....******')
if len(army_user1) == 0 and len(army_user2) == 0:  # Initially if both the armies are empty
    print('Both the armies are empty, Battle is a Tie')

elif len(army_user1) == 0:                         # If army of Player 1 is empty initially
    print('Player 2 Wins the Battle')

elif len(army_user2) == 0:                         # If army of Player 2 is empty initially
    print('Player 1 Wins the Battle')

else:
    round_no = 1
    while flag == 0:                     # while loop keeps running until flag becomes 1, i.e. there is a winner
        if army_user1[0] == 'Archer' and army_user2[0] == 'Archer':     # Similar units
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Round', round_no, 'ends in a Tie')
            if len(army_user1) != 0:
                army_user1.pop(0)          # removes the unit who lost
            if len(army_user2) != 0:
                army_user2.pop(0)
            print_army()                   # prints the updated army after each combat
            winner()                       # shows the winner if one of the armies is empty

        elif army_user1[0] == 'Archer' and army_user2[0] == 'Soldier':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Archer of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
            print_army()
            winner()

        elif army_user1[0] == 'Archer' and army_user2[0] == 'Knight':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print(army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Knight of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
            print_army()
            winner()

        elif army_user1[0] == 'Soldier' and army_user2[0] == 'Archer':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Archer of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
            print_army()
            winner()

        elif army_user1[0] == 'Soldier' and army_user2[0] == 'Soldier':  # Similar units
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Round', round_no, 'ends in a Tie')
            if len(army_user1) != 0:
                army_user1.pop(0)
            if len(army_user2) != 0:
                army_user2.pop(0)
            print_army()
            winner()

        elif army_user1[0] == 'Soldier' and army_user2[0] == 'Knight':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Soldier of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
            print_army()
            winner()

        elif army_user1[0] == 'Knight' and army_user2[0] == 'Archer':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Knight of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
            print_army()
            winner()

        elif army_user1[0] == 'Knight' and army_user2[0] == 'Soldier':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Soldier of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
            print_army()
            winner()

        elif army_user1[0] == 'Knight' and army_user2[0] == 'Knight':  # Similar units
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Round', round_no, 'ends in a Tie')
            if len(army_user1) != 0:
                army_user1.pop(0)
            if len(army_user2) != 0:
                army_user2.pop(0)
            print_army()
            winner()

        round_no += 1        # Increments the round number by 1
