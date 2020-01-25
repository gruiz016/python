import random

# How many guesses player has taken
guessesTaken = 0

# Stores players input into myName
print("Hello! What is your name?")
myName = input()

# Generates random number
number = random.randint(1, 20)

print("Well, " + myName +
      ", I am thinking of a number between 1 and 100.")

for guessesTaken in range(6):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("Good job, " + myName + "! You guessed my number in " +
          guessesTaken + " guesses!")
if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number + ".")
