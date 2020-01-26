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
                ===''']

words = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()

# returns a random work from words


def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


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
missedLetters = ""
correctLetters = ""
secretWords = getRandomWord(words)
gameIsDone = False

# Game loop starts here
while True:
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
            secretWords = getRandomWord(words)
        else:
            break
