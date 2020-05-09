#Problem 5 - Playing a Hand
#10.0/10.0 points (graded)
#In ps4a.py, note that in the function playHand, there is a bunch of pseudocode. This pseudocode is provided to help guide you in writing your function. Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode before you start coding your solution.
#
#Note: Do not assume that there will always be 7 letters in a hand! The parameter n represents the size of the hand.

ef playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
        # Keep track of the total score
    totalScore = 0
    #word =''

    while calculateHandlen(hand) > 0:

        # As long as there are still letters left in the hand
        #if not all (value == 0 for value in hand.values()):
            
            #Display the hand
            print("Current Hand:",end = "")
            displayHand(hand) 

            word = input('Enter word, or a "." to indicate that you are finished: ')
            
            #if the input is '.' break out of the game
            if word == '.': 
                print("Goodbye! Total score:", totalScore, "points.")
                break

            #else if the wors is valid display the score
            elif isValidWord(word, hand, wordList) == True:
                wordScore = getWordScore(word, n)
                totalScore += wordScore
                print ('"'+ word +'"', 'earned', wordScore, 'points.', "Total:", totalScore, "points")
                print(" ")
                hand = updateHand(hand, word)
                if calculateHandlen(hand) == 0:
                    print("Run out of letters. Total score:", totalScore, "points.")
                    print("None")
                    break
            else:
                print("Invalid word, please try again.")
                print(" ")

#Correct 