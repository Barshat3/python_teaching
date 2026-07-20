import random 
import time

choices = ['rock', 'paper', 'scissors']

player_score = 0
computer_score = 0

while True:
    player_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(choices)
    
    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    
    else:
        print("Computer is making its choice...")
        time.sleep(1)  # Simulate thinking time
        print(f"Computer chose: {computer_choice}")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        print(f"Score - You: {player_score}, Computer: {computer_score}")
        
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            print(f"Final Score - You: {player_score}, Computer: {computer_score}")
            break

