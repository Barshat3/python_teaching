import random

players = []
turn = 0
s1=0
s2 = 0 
score = [s1, s2]
turn_score = 0 

target_score = int(input("Enter the target score to win the game: "))
p1 = input("Enter first player name ").title()
p2 = input("Enter second player name ").title()
players.append(p1)
players.append(p2)

while True:
    choice = input(f"{players[turn]}'s({score[turn] + turn_score}) turn. Do you want to roll the dice? (y/n) ").lower()
    if choice == 'y':
        roll = random.randint(1, 6)
        print(f"{players[turn]} rolled a {roll}.")
        if roll == 1:
            print(f"Oops! {players[turn]} rolled a 1. Turn over, no points added.\n")
            turn_score = 0
            turn = 1 - turn  # Switch turns
        else:
            turn_score += roll
            if (score[turn] + turn_score) >= target_score:
                print(f"{players[turn]} wins with a score of {score[turn] + turn_score}!")
                break
            print(f"{players[turn]}'s turn score is now {turn_score}.\n")

    
    elif choice == 'n':
        score[turn] += turn_score
        print(f"{players[turn]} holds. Total score is now {score[turn]}.\n")
        turn_score = 0
        turn = 1 - turn  # Switch turns