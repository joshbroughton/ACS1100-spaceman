import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    #Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    outString = ''
    for letter in secret_word:
        if letter in letters_guessed:
            outString += letter
        else:
            outString += '_'

    return outString

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    game_over = False
    incorrect_guesses = 0
    guess_limit = len(secret_word)
    letters_guessed = []

    #show the player information about the game according to the project spec
    print(f'Welcome to spaceman! Try to fill in the spaces by guessing one letter at a time. If you guess incorrectly {guess_limit} times, you lose!')
    #Ask the player to guess one letter per round and check that it is only one letter
    

    while not game_over:
        valid_guess = False
        while not valid_guess:
            guess = input('Enter a single letter guess: ')
            if guess in letters_guessed:
                print('You already guessed that letter! Enter a different letter; no guess consumed.')
            elif len(guess) == 1 and type(guess) is str:
                valid_guess = True
            else:
                print('Invalid guess. Single letters only! No numbers, special symbols, or words.')

    #Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word) == True:
            print('You\'re guess is in the word!')
        else:
            incorrect_guesses += 1
            print(f'Oh no, the guess isn\'t in the word! {guess_limit - incorrect_guesses} guesses remaining.')
            
        
        letters_guessed.append(guess)

    #show the guessed word so far
        print(f'The word so far is {get_guessed_word(secret_word, letters_guessed)}')
    #check if the game has been won or lost
        if incorrect_guesses >= guess_limit:
            print('More than 7 incorrect guesses have been made, sorry, you lose!')
            game_over = True
        elif is_word_guessed(secret_word, letters_guessed) == True:
            print('Great job, you guessed the word!')
            game_over = True


#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
