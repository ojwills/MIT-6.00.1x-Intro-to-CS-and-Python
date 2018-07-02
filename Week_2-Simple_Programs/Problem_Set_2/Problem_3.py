#Problem 3 - Printing Out all Available Letters
#10.0/10.0 points (graded)
#Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.
#
#Example Usage:
#
#>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#>>> print(getAvailableLetters(lettersGuessed))
#abcdfghjlmnoqtuvwxyz
#Note that this function should return the letters in alphabetical order, as in the example above.
#
#For this function, you may assume that all the letters in lettersGuessed are lowercase.

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    from string import ascii_lowercase as alphabet
    alphabetList = list(alphabet) 
    for letter in lettersGuessed:
        if letter in alphabetList:
            alphabetList.remove(letter)
    alphabetString = ''.join(alphabetList)
    return alphabetString            

#Complete