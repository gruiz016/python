import random
import time


def displayIntro():
    print("You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.")
    print()

# Stores players choice


def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you go into? (1 or 2)")
        cave = input()
    return cave

# Checks cave, and randimizes which cave has enemy


def checkCave(chosenCave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and....")
    time.sleep(2)
    print()

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("Gives you his treasure!")
    else:
        print("Eat's you up in one bite!")

# Game play execution


playAgain = "yes"

while playAgain == "yes" or playAgain == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print("Would you like to play again? (yes or no)")
    playAgain = input()
