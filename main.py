import random 

computer_score = 0
player_score = 0

while True:

    print("Computer Will Select Between Snake, Water and Gun Randomly!") 
    print("You Have To Select The Choices Given Below!") 

    # Mapping integers to choices for both computer and player
    choices = {-1: "Snake", 0: "Gun", 1: "Water"}

    # Random selection for computer
    comp = random.randint(-1, 1) 

    print("Select '-1' for Snake, 0 for 'Gun' and 1 for 'Water'") 

    player = None

    # Ensuring valid player input
    while player not in [-1, 0, 1]:
        try:
            player = int(input(""))
        except ValueError:
            print("Invalid Input! Please enter a number.")
        finally:
            print("Please Enter a Correct Numeric Value From the Choices Given Above! ")

    print(f"Player has Choosen {choices[player]}")
    print(f"Computer has Choosen {choices[comp]} ")

    # Game outcomes
    a = "It's a Draw"
    b = "Computer Wins" 
    c = "Player Wins"

    if comp == player:
        print(a)
    elif comp == 0 and player == -1 or comp == -1 and player == 1 or comp == 1 and player == 0: 
        print(b)
        computer_score += 1
        print(f"Computer's Score is {computer_score}! ")
    elif comp == 0 and player == 1 or comp == -1 and player == 0 or comp == 1 and player == -1: 
        print(c)    
        player_score += 1
        print(f"Player's Score is {player_score}! ")
    else:
        print("Please Select the correct option!")

    # Replay prompt
    while True:
        play_again = input("Do you want to play again? Press letter 'y' to play again or 'n' to quit the game: ")

        if play_again.lower() == "n":
            break
        elif play_again.lower() == "y":
            break
        else:
            print("Invalid input. Please type 'y' to continue or 'n' to quit.")
    if play_again.lower() == "n":
        break

# Final score announcement
if player_score > computer_score:
    print("Player Has Won!")
elif player_score < computer_score:
    print("Computer Has Won!")
elif player_score == computer_score:
    print("Game ended in a Draw — Equal Scores!")

