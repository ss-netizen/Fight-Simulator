"""
WRITTEN BY - SHIVAM PRATAP SINGH
STUDENT ID - 29565413
VERSION - PYTHON 3
START DATE - 16-08-2018
LAST UPDATE - 23-08-2018

This is the advanced version of the combat simulator. This has all the features of the basic game but additionally
2 new features are implemented : Medics and Expanded Armies
Medics is automatically assigned to every player with the amount that is left with him after he has bought his Final Army.
Medics has the power to revive the unit that dies in a combat until the medics itself exhausts. 1 Medic can only be
used to revive a unit only once.
The Expanded Armies introduces 2 new units : Siege Equipment and Wizard that have different strengths and weaknesses.
So, the cost of each unit is changed according to its strength.
Then the game progresses the same way as in Basic Game but now, the result of the battles is decided based on a new and
updated outcomes table.
The winner is decided the same way as it was decided in the Basic Game.
"""


global flag
flag = 0

"""
This is the menu() function, it shows the units available for the players to select.
"""


def menu():
    print("\nUnits available for purchase :\n")
    print("1. Archer (Price : $2)")      # New Prices for units based on their strengths
    print("2. Soldier (Price : $1)")
    print("3. Knight (Price : $2)")
    print("4. Siege Equipment (Price : $2)")
    print("5. Wizard (Price : $3)")
    print("6. Exit\n")


# Taking input from Player 1

# The initial amount for the player to begin with is assigned as $10
funds_user1 = 10
army_user1 = []
menu()
print("Player 1 : \nEnter which unit you want to buy by pressing 1,2,3,4 or 5 (Press 6 for exit) :")

# The while loop keeps running until all funds are finished.
while funds_user1 > 0:
    print('Funds available = $', funds_user1)
    user1_input = input('Enter your choice:')

# Adds the unit to the army based on the player's selection and then decrements the fund by pre-set value for every unit bought
    if user1_input == '1':
        if funds_user1 >= 2:
            army_user1.append('Archer')
            funds_user1 -= 2
        else:
            print('Insufficient funds for buying Archer')

    if user1_input == '2':
        army_user1.append('Soldier')
        funds_user1 -= 1

    if user1_input == '3':
        if funds_user1 >= 2:
            army_user1.append('Knight')
            funds_user1 -= 2
        else:
            print('Insufficient funds for buying Knight')

    if user1_input == '4':
        if funds_user1 >= 2:
            army_user1.append('Siege Equipment')
            funds_user1 -= 2
        else:
            print('Insufficient funds for buying Siege Equipment')

    if user1_input == '5':
        if funds_user1 >= 3:
            army_user1.append('Wizard')
            funds_user1 -= 3
        else:
            print('Insufficient funds for buying Wizard')

    if user1_input == '6':
        break

    if user1_input != '1' and user1_input != '2' and user1_input != '3' and user1_input != '4' and user1_input != '5' and user1_input != '6':
        print('Enter correct input')
        menu()

    print('Player 1 Army :', army_user1)
print('\nPlayer 1 final Army :', army_user1)
print('Funds left : $', funds_user1)
medics_user1 = funds_user1   # Buy the medics with the funds that are left
print('\nMedics available for Player 1:', medics_user1, '(1 Medic = $1)')
print("\n")

# Taking input from Player 2

# The initial amount for the player to begin with is assigned as $10
menu()
funds_user2 = 10
army_user2 = []
print("Player 2 : \nEnter which unit you want to buy by pressing 1,2,3,4 or 5 (Press 6 for exit) :")

while funds_user2 > 0:
    print('Funds available = $', funds_user2)
    user2_input = input('Enter your choice:')

    if user2_input == '1':
        if funds_user2 >= 2:
            army_user2.append('Archer')
            funds_user2 -= 2
        else:
            print('Insufficient funds for buying Archer')

    if user2_input == '2':
        army_user2.append('Soldier')
        funds_user2 -= 1

    if user2_input == '3':
        if funds_user2 >= 2:
            army_user2.append('Knight')
            funds_user2 -= 2
        else:
            print('Insufficient funds for buying Knight')

    if user2_input == '4':
        if funds_user2 >= 2:
            army_user2.append('Siege Equipment')
            funds_user2 -= 2
        else:
            print('Insufficient funds for buying Siege Equipment')

    if user2_input == '5':
        if funds_user2 >= 3:
            army_user2.append('Wizard')
            funds_user2 -= 3
        else:
            print('Insufficient funds for buying Wizard')

    if user2_input == '6':
        break

    if user2_input != '1' and user2_input != '2' and user2_input != '3' and user2_input != '4' and user2_input != '5' and user2_input != '6':
        print('Enter correct input')
        menu()

    print('Player 2 Army :', army_user2)
print('\nPlayer 2 final Army :', army_user2)
print('Funds left : $', funds_user2)
medics_user2 = funds_user2
print('\nMedics available for Player 2:', medics_user2, '(1 Medic = $1)')

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
        print('Player 2 Wins the battle')
        flag = 1
    elif len(army_user1) == 0 and len(army_user2) == 0:  # All units in both armies are finished
        print(".....Both the armies are dead, Battle ends in a Tie.....")
        flag = 1

# Combat begins
print('\n')
print('******.....Battle begins.....******')
if len(army_user1) == 0 and len(army_user2) == 0:  # Initially if both the armies are empty
    print('Both the armies are empty, Battle is a Tie')

elif len(army_user1) == 0:                        # If army of Player 1 is empty initially
    print('Player 2 Wins the battle')

elif len(army_user2) == 0:                        # If army of Player 2 is empty initially
    print('Player 1 Wins the battle')

else:
    round_no = 1
    while flag == 0:                 # while loop keeps running until flag becomes 1, i.e. there is a winner

        # For Archer

        if army_user1[0] == 'Archer' and army_user2[0] == 'Archer':     # Similar units
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Round', round_no, 'ends in a Tie')
            if len(army_user1) != 0:
                army_user1.pop(0)           # removes the unit who lost
                if medics_user1 != 0:                         # Check if user has medics left
                    army_user1.append('Archer')
                    print('Archer of Army 1 Revived')
                    medics_user1 -= 1           # Keep on decrementing medics for every revival
                    print('Medics Left for Player 1 =', medics_user1)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                         # Check if user has medics left
                    army_user2.append('Archer')
                    print('Archer of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()                              # prints the updated army after each combat
            winner()                                  # shows the winner if one of the armies is empty

        elif army_user1[0] == 'Archer' and army_user2[0] == 'Soldier':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Archer of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Soldier')
                    print('Soldier of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        elif army_user1[0] == 'Archer' and army_user2[0] == 'Knight':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Knight of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Archer')
                    print('Archer of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            print_army()
            winner()

        elif army_user1[0] == 'Archer' and army_user2[0] == 'Siege Equipment':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Siege Equipment of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Archer')
                    print('Archer of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            print_army()
            winner()

        elif army_user1[0] == 'Archer' and army_user2[0] == 'Wizard':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Archer of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Wizard')
                    print('Wizard of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

# For Soldier
        elif army_user1[0] == 'Soldier' and army_user2[0] == 'Archer':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Archer of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Soldier')
                    print('Soldier of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            print_army()
            winner()

        elif army_user1[0] == 'Soldier' and army_user2[0] == 'Soldier':  # Similar units
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Round', round_no, 'ends in a Tie')
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Soldier')
                    print('Soldier of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Soldier')
                    print('Soldier of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        elif army_user1[0] == 'Soldier' and army_user2[0] == 'Knight':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Soldier of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Knight')
                    print('Knight of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        elif army_user1[0] == 'Soldier' and army_user2[0] == 'Siege Equipment':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Siege Equipment of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Soldier')
                    print('Soldier of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            print_army()
            winner()

        elif army_user1[0] == 'Soldier' and army_user2[0] == 'Wizard':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Wizard of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Soldier')
                    print('Soldier of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            print_army()
            winner()

# For Knight
        elif army_user1[0] == 'Knight' and army_user2[0] == 'Archer':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Knight of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Archer')
                    print('Archer of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        elif army_user1[0] == 'Knight' and army_user2[0] == 'Soldier':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Soldier of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Knight')
                    print('Knight of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            print_army()
            winner()

        elif army_user1[0] == 'Knight' and army_user2[0] == 'Knight':  # Similar units
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Round', round_no, 'ends in a Tie')
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Knight')
                    print('Knight of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Knight')
                    print('Knight of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        elif army_user1[0] == 'Knight' and army_user2[0] == 'Siege Equipment':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Knight of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Siege Equipment')
                    print('Siege Equipment of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        elif army_user1[0] == 'Knight' and army_user2[0] == 'Wizard':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Wizard of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Knight')
                    print('Knight of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            print_army()
            winner()

# For Siege Equipment
        elif army_user1[0] == 'Siege Equipment' and army_user2[0] == 'Archer':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Siege Equipment of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Archer')
                    print('Archer of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        elif army_user1[0] == 'Siege Equipment' and army_user2[0] == 'Soldier':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Siege Equipment of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Soldier')
                    print('Soldier of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        elif army_user1[0] == 'Siege Equipment' and army_user2[0] == 'Knight':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Knight of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Siege Equipment')
                    print('Siege Equipment of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            print_army()
            winner()

        elif army_user1[0] == 'Siege Equipment' and army_user2[0] == 'Siege Equipment':  # Similar units
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Round', round_no, 'ends in a Tie')
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Siege Equipment')
                    print('Siege Equipment of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Siege Equipment')
                    print('Siege Equipment of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        elif army_user1[0] == 'Siege Equipment' and army_user2[0] == 'Wizard':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Wizard of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Siege Equipment')
                    print('Siege Equipment of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            print_army()
            winner()

# For Wizard
        elif army_user1[0] == 'Wizard' and army_user2[0] == 'Archer':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Archer of Army 2 wins Round', round_no)
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Wizard')
                    print('Wizard of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            print_army()
            winner()

        elif army_user1[0] == 'Wizard' and army_user2[0] == 'Soldier':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Wizard of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Soldier')
                    print('Soldier of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        elif army_user1[0] == 'Wizard' and army_user2[0] == 'Knight':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Wizard of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Knight')
                    print('Knight of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        elif army_user1[0] == 'Wizard' and army_user2[0] == 'Siege Equipment':
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Wizard of Army 1 wins Round', round_no)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Siege Equipment')
                    print('Siege Equipment of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        elif army_user1[0] == 'Wizard' and army_user2[0] == 'Wizard':  # Similar units
            print("\nRound", round_no, ": ", army_user1[0], "of Army 1 versus", army_user2[0], "of Army 2")
            print('Round', round_no, 'ends in a Tie')
            if len(army_user1) != 0:
                army_user1.pop(0)
                if medics_user1 != 0:                        # Check if user has medics left
                    army_user1.append('Wizard')
                    print('Wizard of Army 1 Revived')
                    medics_user1 -= 1
                    print('Medics Left for Player 1 =', medics_user1)
            if len(army_user2) != 0:
                army_user2.pop(0)
                if medics_user2 != 0:                        # Check if user has medics left
                    army_user2.append('Wizard')
                    print('Wizard of Army 2 Revived')
                    medics_user2 -= 1
                    print('Medics Left for Player 2 =', medics_user2)
            print_army()
            winner()

        round_no += 1               # Increments the round number by 1
