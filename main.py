import random

choices = ('r', 'p', 's')
computerScore = 0
playerScore = 0


def player_choice():
    choice = input("Select rock, paper or scissors (r, p, s): ")
    if choice == 'r' or choice == 'p' or choice == 's':
        return choice
    else:
        return player_choice()


def computer_choice():
    global choices
    choice = random.choice(choices)
    return choice


def game():
    global playerScore
    global computerScore
    print("Player score: {}".format(playerScore))
    print("Computer score: {}".format(computerScore))
    pc = player_choice()
    cc = computer_choice()
    print("Your choice: {}\ncomputer choice: {}".format(pc, cc))
    if pc == cc:
        print("TIE")
    elif (pc == 'r' and cc == 's') or (pc == 's' and cc == 'p') or (pc == 'p' and cc == 'r'):
        print("Player wins")
        playerScore += 1
    else:
        print("Computer wins")
        computerScore += 1


print("Welcome to the game!!!")
while True:
    for i in range(4):
        game()
    print("Do you want continue or reset score or quit? ")
    menu = input("press r to reset q to quit: ")
    if menu == 'q':
        print("Byee")
        print("Final score: \nPlayer: {}\nComputer: {}".format(playerScore, computerScore))
        break
    elif menu == "r":
        playerScore = 0
        computerScore = 0
