import random

invalidMax = 3
invalidAttempts = 0
invalidAttemptsRem = 0

options = ("rock", "paper", "scissors")

while True:

    player = None
    computer = random.choice(options)
    print ("Welcome to Rock Paper Scissors")
    print ("==============================")
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
        if player not in options:
            invalidAttempts += 1
            print("Invalid anwser! Please try again!")
            invalidAttemptsRem = invalidMax - invalidAttempts
            print (f"You have {invalidAttemptsRem} attempts remaining")

            if invalidAttempts == invalidMax:
                  print ("===========================================")
                  print("Too many invalid attempts. Exiting the game!")
                  print ("===========================================")
                  quit()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'yes' and play_again.lower() != 'y':
        break
    else:
        continue

print("Thanks for playing!")