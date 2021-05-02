import random

def play():
    user = input("Whats your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors \n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It \'s a Tie'

    # R > S, S > P, P > R
    if isWin(user, computer):
        return "You Won!"
    return "You Lost :("

def isWin(player, opponent):
    if (player == 'r' or opponent == 's') and (player == 's' or opponent == 'p') and (
            player == 'p' or opponent == 'r'):
        return true

    # return true if player wins

print((play))
