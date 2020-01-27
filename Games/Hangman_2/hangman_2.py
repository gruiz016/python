import random

HANGMAN_PICS = ['''
            +---+
	            |
	            |
	            |
	            ===''', '''
            +---+		
            O   |		
                |		
                |		
                ===''', '''		
            +---+		
            O   |		
            |   |		
                |		
                ===''', '''		
            +---+		
            O   |		
           /|   |		
                |		
                ===''', '''		
            +---+		
            O   |		
           /|\  |		
                |		
                ===''', '''		
            +---+		
            O   |		
           /|\  |		
            /    |		
                ===''', '''		
            +---+		
            O   |		
           /|\  |		
           / \  |		
                ===''', '''		
            +---+		
           [O   |		
           /|\  |		
           / \  |		
                ===''', '''		
            +---+		
           [O]  |		
           /|\  |		
           / \  |		
                ===''']

wordDict = {"Colors": "red yellow blue green black brown silver".split(), "Shapes": "circle triangle square rectangle oval". split(
), "Fruit": "apple organge lemon blueberry strawberry grape pineapple mango".split(), "Animals": "cat dog snake lion tiger bear bird".split()}

# returns a random work from words


def getRandomWord(wordList):
    # Returns a random string from the dictionary
    wordKey = random.choice(list(wordDict.keys()))
    # Randomly select a work from the key list in the dictionary
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]


def displayBoard(missedLetters, correctLetter, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print("Missed letters:", end=" ")

    # Add's a space between guessed letters
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    # Creates blanks based on word
    blanks = "_" * len(secretWord)

    # Replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetter:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    # Re-prints the blanks with correct letters
    for letter in blanks:
        print(letter, end=" ")
        print()


def getGuesses(alreadyGuessed):
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You already guessed that letter, please guess again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter.")
        else:
            return guess


def playAgain():
    print("Would you like to play again? (Yes or No)")
    return input().lower().startswith("y")


# Game logic starts here
print("H A N G M A N")

# Setting difficulty of the game
difficulty = "X"
while difficulty not in "EMH":
    print("Enter difficulty: E - Easy, M - Medium, H - Hard.")
    difficulty = input().upper()
if difficulty == "M":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == "H":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ""
correctLetters = ""
secretWords, secretSet = getRandomWord(wordDict)
gameIsDone = False

# Game loop starts here
while True:
    print("The secret word is in the set: " + secretSet)
    displayBoard(missedLetters, correctLetters, secretWords)

    # Let the player enter a letter.
    guess = getGuesses(missedLetters + correctLetters)

    if guess in secretWords:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWords)):
            if secretWords[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' +
                  secretWords + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWords)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses. The word was "' + secretWords + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWords, secretSet = getRandomWord(wordDict)
        else:
            break
