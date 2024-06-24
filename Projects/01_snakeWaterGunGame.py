import random

# SNAKE, WATER, GUN GAME

"""
snake beats water, water beats gun, and gun beats snake
CHARACTER       USER        COMPUTER        WIN          
SNAKE             S             W            S U
                  S             G            G C  
                  S             S            DRAW       
WATER             W             S            S C      
                  W             G            W U  
                  W             W            DRAW       
RUN               G             S            G U      
                  G             W            W C      
                  G             G            DRAW       
"""


def snakeWaterGun(user, computer):

    if user == computer:
        print("Game Draw")
    elif (
        (user == "s" and computer == "w") 
        or (user == "w" and computer == "g") 
        or (user == "g" and computer == "s") 
    ):
        print("***** You Win *****")
    elif (
        (user == "s" and computer == "g")
        or (user == "w" and computer == "s")
        or (user == "g" and computer == "w")
    ):
        print("***** Computer Win *****")
    else:
        print("invalid input")


lst = ["s", "g", "w"]
while True:
    computer = random.choice(lst)
    user = input("Choose s, w, g or press c for exit: ").lower()
    if user == "c":
        break
    elif user not in lst:
        print("Invalid input. Please choose 's', 'w', or 'g'.")
    snakeWaterGun(user, computer)
