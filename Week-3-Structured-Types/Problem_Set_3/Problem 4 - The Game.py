#Problem 4 - The Game
#12.0/15.0 points (graded)
#Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.
#
#Hints:
#You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your hangman function.
#
#Consider using lower() to convert user input to lower case. For example:
#
#guess = 'A'
#guessInLowerCase = guess.lower()
#Consider writing additional helper functions if you need them!
#
#There are four important pieces of information you may wish to store:
#
#secretWord: The word to guess.
#lettersGuessed: The letters that have been guessed so far.
#mistakesMade: The number of incorrect guesses made so far.
#availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = [""]
    guessedWord = [""]
    char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    mistakesMade = 0
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("----------")
    
    while guessedWord != secretWord:
        
        print("You have", str(8 - mistakesMade), "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        x = (input("Please guess a letter: ")).lower()
        
        if x in lettersGuessed:
            print("Oops! You've already guessed that letter:", guessedWord)
            print("-----------")
            #lettersGuessed += x
        else:    
            lettersGuessed += x
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            
            if isWordGuessed(lettersGuessed, secretWord) is True:
                print("Good guess:", guessedWord)
                print("----------")
                if len(secretWord) ==1:
                    break
            else:
                print("Oops! That letter is not in my word:", guessedWord)
                print("----------")
                mistakesMade += 1
                if mistakesMade > 7:
                   return print("Sorry, you ran out of guesses. The word was:", secretWord)
                    
    return print("Congratulations, you won!")

#Correct 