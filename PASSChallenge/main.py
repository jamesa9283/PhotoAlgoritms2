import random


def guessed():
    userInput = int(input("Your guess please: "))
    if userInput == randomNumber:
        print("Correct, You win!")
        return True
    elif userInput not in range(0, 100):
        print("Our guess range is between 0 and 100")
    elif userInput > randomNumber:
        print("Try one more time, a bit lower")
    elif userInput < randomNumber:
        print("Try one more time, a bit higher")
    return False


randomNumber = random.randrange(0, 100)

print("Random number has been generated")
while not guessed():
    guessed()
