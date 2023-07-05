# warm up before RPS
# a = 5
# while (a > 0):
#     print(a)
#     a-=1

# quit = input('Type "enter" to quit \n')
# while quit != "enter":
#     quit=input('Type "enter" to quit \n')

# while True:
#     usr_command = input("Enter a command: \n")
#     if usr_command == quit:
#         break
#     else:
#         print("You typed: " + usr_command + "\n")

import sys

def compare(p1, p2):
    if p1 == p2:
        return("It's a tie!")
    elif p1 == 'rock':
        if p2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif p1 == 'scissors':
        if p2 == 'paper':
            return("Scissors wins!")
        else:
            return("Rock wins!")
    elif p1 == 'paper':
        if p2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors wins!")
    else:
        return("Invalid input. Please choose rock, paper, or scissors.\n")

player1 = input("Enter first player name: \n")
player2 = input("Enter second player name: \n")

player1_score = 0
player2_score = 0

for round in range(3):
    print(f"\n--- Round {round+1} ---")
    player1_hand = input("%s, pick rock, paper, or scissors: " % player1)
    player2_hand = input("%s, pick rock, paper, or scissors: " % player2)

    result = compare(player1_hand, player2_hand)

    if "wins" in result:
        print(result)
        if result == "Rock wins!" or result == "Paper wins!" or result == "Scissors wins!":
            player1_score += 1
        else:
            player2_score += 1
    else:
        print(result)

print("\n--- Final Game ---")
if player1_score > player2_score:
    print(f"{player1} wins the game!")
elif player1_score < player2_score:
    print(f"{player2} wins the game!")
else:
    print("The game ends in a tie!")
