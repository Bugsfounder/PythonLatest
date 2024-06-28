import random


def game():
    computerGuess = random.randint(1, 100)
    userTries = 0
    while True:
        userInput = int(input("Enter the Number: "))
        if userInput > 0 and userInput <= 100:
            if userInput > computerGuess:
                print("Lower number please")
                userTries += 1
            elif userInput < computerGuess:
                print("higher number please")
                userTries += 1
            elif userInput == computerGuess:
                userTries += 1
                print(f"You taken {userTries} attempts to guess the correct number")
                print("correct number")
                break
        else:
            print("The number is must be greater than 0 and less than or equals to 100")


game()
