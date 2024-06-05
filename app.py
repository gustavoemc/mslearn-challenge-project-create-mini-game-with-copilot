import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def get_player_choice():
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").strip().lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid choice. Please try again.")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"

def play_game():
    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(player_choice, computer_choice)
        
        if winner == "player":
            print("You win this round!")
            player_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        rounds += 1
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

    print(f"\nFinal score:\nYou: {player_score}\nComputer: {computer_score}\nTotal rounds: {rounds}")

if __name__ == "__main__":
    play_game()
