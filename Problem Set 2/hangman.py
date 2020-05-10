# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False 
    # returning False if a charater from secret_word is not in letters_guessed
    
    return True #returning true otherwise    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed = ''
    for char in secret_word:
        if char in letters_guessed:
            guessed = guessed + char # adding the character to the string if it is guessed
        else:
            guessed = guessed + '_ ' # adding a '_ ' otherwise
            
    return guessed 



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    lower = 'abcdefghijklmnopqrstuvwxyz'
    available = ''
    for char in lower:
        if char not in letters_guessed:
            available = available + char 
            #putting the unguessed letters together
            
    return available
    
    

def hangman(secret_word):    
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    length = len(secret_word)
    print("Welcome to the game Hangman!")
    print('I am thinking of a word that is ' + str(length) + ' letters long.') 
    print('You have 3 warnings left.')
    print('-------------')
    letters_guessed = []
    numGuesses = 6
    numWarnings = 3
    unique = ''
    for char in secret_word:
        if char not in unique:
            unique = unique + char
    unique_length = len(unique)
    
    while(not is_word_guessed(secret_word, letters_guessed) and numGuesses > 0):
        
        print('You have ' + str(numGuesses) + ' guesses left')
        print('Available letters: ' + get_available_letters(letters_guessed))
        guessed_letter = input('Please guess a letter: ')
        guessed_letter = guessed_letter.lower()
        
        if not guessed_letter.isalpha():
            if numWarnings >= 1:
                numWarnings -= 1
                print('Oops! That is not a valid letter. You have ' + 
                      str(numWarnings) + ' warnings left: ' + get_guessed_word(
                              secret_word, letters_guessed))
            else:
                print('You have no warnings left, so you lose a guess: ' + 
                      get_guessed_word(secret_word, letters_guessed))
                numGuesses -= 1
        
        elif guessed_letter in letters_guessed:
            if numWarnings >= 1:
                numWarnings -= 1
                print("Oops! You've already guessed that letter. You have " + 
                      str(numWarnings) + ' warnings left: ' + get_guessed_word(
                              secret_word, letters_guessed))
            else:
                print('You have no warnings left, so you lose a guess: ' + 
                      get_guessed_word(secret_word, letters_guessed))
                numGuesses -= 1
            
        elif guessed_letter in secret_word:
            letters_guessed.append(guessed_letter)
            print('Good guess: ' + get_guessed_word(
                    secret_word, letters_guessed))
            
        else:
            letters_guessed.append(guessed_letter)
            print('Oops! That letter is not in my word.')
            print('Please guess a letter: ' + get_guessed_word(
                     secret_word, letters_guessed))
            if guessed_letter in ['a','e','i','o','u']:
                numGuesses -= 2
            else:
                numGuesses -= 1
            
        
        print('-------------')
        
    
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print('Your total score for this game is: ' + str(numGuesses * 
                                                          unique_length))
    else:
        print('Sorry, you ran out of guesses. The word is was ' + 
              secret_word)
         
                
                
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    word = ''
    for char in my_word:
        if char != ' ':                    # a_ple     a__le 
            word += char                    #apple     apple
            
    if len(word) != len(other_word):
        return False
    
    for i in range(len(other_word)):
        if word[i] != '_':
            if word[i] != other_word[i]:
                return False
            #if word[i] 
        else:
            if other_word[i] in word:
                return False
            
    return True
    

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    f = 0
    for word in wordlist:
        if match_with_gaps(my_word, word):
            f = 1
            print(word)
            
    if f == 0:
        print("No matches found")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    length = len(secret_word)
    print("Welcome to the game Hangman!")
    print('I am thinking of a word that is ' + str(length) + ' letters long.') 
    print('You have 3 warnings left.')
    print('-------------')
    letters_guessed = []
    numGuesses = 6
    numWarnings = 3
    unique = ''
    for char in secret_word:
        if char not in unique:
            unique = unique + char
    unique_length = len(unique)
    
    while(not is_word_guessed(secret_word, letters_guessed) and numGuesses > 0):
        
        print('You have ' + str(numGuesses) + ' guesses left')
        print('Available letters: ' + get_available_letters(letters_guessed))
        guessed_letter = input('Please guess a letter: ')
        guessed_letter = guessed_letter.lower()
        
        if guessed_letter == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        
        elif not guessed_letter.isalpha():
            if numWarnings >= 1:
                numWarnings -= 1
                print('Oops! That is not a valid letter. You have ' + 
                      str(numWarnings) + ' warnings left: ' + get_guessed_word(
                              secret_word, letters_guessed))
            else:
                print('You have no warnings left, so you lose a guess: ' + 
                      get_guessed_word(secret_word, letters_guessed))
                numGuesses -= 1
        
        elif guessed_letter in letters_guessed:
            if numWarnings >= 1:
                numWarnings -= 1
                print("Oops! You've already guessed that letter. You have " + 
                      str(numWarnings) + ' warnings left: ' + get_guessed_word(
                              secret_word, letters_guessed))
            else:
                print('You have no warnings left, so you lose a guess: ' + 
                      get_guessed_word(secret_word, letters_guessed))
                numGuesses -= 1
            
        elif guessed_letter in secret_word:
            letters_guessed.append(guessed_letter)
            print('Good guess: ' + get_guessed_word(
                    secret_word, letters_guessed))
            
        else:
            letters_guessed.append(guessed_letter)
            print('Oops! That letter is not in my word.')
            print('Please guess a letter: ' + get_guessed_word(
                     secret_word, letters_guessed))
            if guessed_letter in ['a','e','i','o','u']:
                numGuesses -= 2
            else:
                numGuesses -= 1
            
        
        print('-------------')
        
    
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print('Your total score for this game is: ' + str(numGuesses * 
                                                          unique_length))
    else:
        print('Sorry, you ran out of guesses. The word is was ' + 
              secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    #secret_word = 'else'
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    
