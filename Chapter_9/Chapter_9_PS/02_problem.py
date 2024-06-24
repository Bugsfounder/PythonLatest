import random


def game():
    score = random.randint(1, 100)
    print(score)
    hiscore = 0
    # Read hiscore.txt
    with open("Chapter_9/Chapter_9_PS/hiscore.txt") as fs:
        hiscore = fs.read()
        
    if hiscore == "":
        hiscore = 0

    if score > int(hiscore):
        with open("Chapter_9/Chapter_9_PS/hiscore.txt", "w") as fs:
            fs.write(str(score))


game()
