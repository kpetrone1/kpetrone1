# Class homework assignment for "Problem Solving and Software Design" with Prof. Li
# Made with assistance from Prof. Li and Internet
# Hangman game
# -----------------------------------
# Helper code
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():                                    # defines the function "loadWords"
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")         # informs user that file of words is loading
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')           
    # line: string
    line = inFile.readline()                        # defines the variable "line" as a line in the file "WORDLIST_FILENAME" (note: "WORDLIST_FILENAME" = "words.txt")
    # wordlist: list of strings
    wordlist = line.split()                         # "separates" the words in a single line
    print("  ", len(wordlist), "words loaded.")     # prints a series of spaces, the number of elements in the list (the number of words in "wordlist"), and the phrase "words loaded."
    return wordlist                                 # "Returns a list of valid words. Words are strings of lowercase letters."

def chooseWord(wordlist):
    """"
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)                  # uses the "choice" function from the "random" library to select a random element (word) from the argument (the list titled "wordlist") and return it
# end of helper code
# -----------------------------------

wordlist = loadWords()                              

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;  # boolean = type of return (true or false)
      False otherwise
    '''
    for letter in secretWord:                       # for each letter in the secret word...
        if letter not in lettersGuessed:            # ...if it is not also in the list of lettersGuessed, then...
            return False                            # ...return False to indicate that not all of the letters in the secret word have been guessed
    return True                                     # otherwise, return True to indicate that all of the letters in the secret word have been guessed

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = ''                                          # define "s" as a new, empty string
    for letter in secretWord:                       # for each letter in the secret word,...
        if letter in lettersGuessed:                # ...if the letter is also in the list of lettersGuessed, then...
            s += letter                             # ...add that letter to the output string "s", which is the "string, comprised"...
                                                    # ..."of letters and underscores that represents what letters in secretWord have been guessed so far"
        else:                                       # otherwise, if the letter in the secretWord has not yet been guessed because it is not in the list of lettersGuessed, then...
            s += '_ '                               # ...add an underscore to the output string "s"
    return s                                        # return the string of letters and underscores where letters indicate letters in the secret word that...
                                                    # ...have correctly been guessed and underscores indicate letters in the secret word that have not yet been guessed

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string                                               # import the string library         

    available_letters = ''                                      # create a new string titled "available_letters"

    for letter in string.ascii_lowercase:                       # for each letter in the string "ascii_lowercase," which is a string of the lowercase letters in the alphabet,...
        if letter not in lettersGuessed:                        # if the letter is not in the list of lettersGuessed, then...
            available_letters = available_letters + letter      # ...add that letter to the string titled "available_letters"
        else:                                                   # otherwise,...
            pass                                                # ...do not do anything
    return available_letters                                    # return the string of available letters

def hangman(secretWord): 
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    Runs a game of hangman between a user and the computer. The computer
    randomly selects a word from the word list. The code gives the user
    a specified number of letter guesses (in this case, eight guesses) to
    guess the word.
    '''

    import string                                                                                                   # import string library so we can use predefined strings of the alphabet ("string.ascii_lowercase" and "string.ascii_uppercase")
    print("Welcome to the game, Hangman!")                                                                          # welcome user to game
    print("I am thinking of a word that is {} letters long." .format(len(secretWord)))                              # inform user of number of letters in secret word (determined using length, or "len", function)
    print("----------")
    number_of_guesses = 8                                                                                           # define variable "number_of_guesses" to 8 to restrict number of guesses    
    lettersGuessed = []                                                                                             # create new list to store letters guessed

    while number_of_guesses > 0:                                                                                    # while number of guesses is positive...
        if isWordGuessed(secretWord, lettersGuessed) == True:                                                       # ...if secret word has correctly been guessed...
            print("Congratulations! You've won: ", getGuessedWord(secretWord, lettersGuessed))                      # ...congratulate user and print secret word as guessed
            break                                                                                                   # if secret word has been guessed, exit the "while" loop
        else:                                                                                                       # if secret word has not been guessed...
            print("You have {} guesses left." .format(number_of_guesses))                                           # ...inform user of number of guesses remaining
            print("Available letters: ", getAvailableLetters(lettersGuessed))                                       # inform user of letters that have not yet been guessed
            guess = input("Please guess a letter: ")                                                                # ask user for a letter and set that letter equal to the new variable titled "guess"
            if guess not in (string.ascii_lowercase or string.ascii_uppercase):                                     # if input is not a letter (either lowercase or uppercase)...
                print("Only letters should be entered. Pleaese do not enter numbers or other characters.")          # ...inform user that only letters should be entered
                print("----------")
            else:                                                                                                   # else, if input is a letter,...
                if guess in lettersGuessed:                                                                         # ...and if letter has already been guessed...
                    print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord,lettersGuessed))  # ...inform user that that letter has already been guessed and print most updated string of letters and underscores
                    print("----------")
                else:                                                                                               # else, if input letter has not already been guessed...
                    if guess in secretWord:                                                                         # ...if input letter is in secret word...
                        lettersGuessed.append(guess)                                                                # ...add that letter to list of guessed letters
                        print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))                           # inform user that that letter is in secret word and print updated string of letters and underscores
                        print("----------")
                    else:                                                                                           # else, if input letter is not in secret word...
                        lettersGuessed.append(guess)                                                                # ...still add it to list of guessed letters
                        number_of_guesses -= 1                                                                      # deduct a guess from number of guesses remaining
                        print("Oops! That letter is not in my word: ", getGuessedWord(secretWord,lettersGuessed))   # inform user that that input letter is not in secret word and print most updated string of letters and underscores
                        print("----------")
    if isWordGuessed(secretWord, lettersGuessed) == False:                                                          # while number of guesses is no longer positive (aka number of guesses equals zero), if secret word has still not yet been guessed,...
        print("Sorry. You've run out of guesses. The word was {}." .format(secretWord))                             # ...notify user that no more guesses remain and inform user of secret word
    
secretWord = chooseWord(wordlist).lower()                                                                           # define variable "secretWord" as a randomly chosen word from the "wordlist" found using the "chooseWord" function defined above
hangman(secretWord)                                                                                                 # run hangman function for secret word
