from random import choice

guessed_letters = []
wrong_letters = []
tries = 0

def get_word():
    words = []
    with open('words.txt', 'r') as file:
        words = file.readlines()

    rand_word = choice(words)
    word = list(rand_word.strip())
    return word


def first_hint(word):
    print(f'This is your word to guess:')
    for _ in range(len(word)):
        print('_ ', end='')


def ask_for_letter():
    print('')
    letter = input('Type a letter: ')
    if len(letter) != 1:
        print('Just one letter please')
        ask_for_letter() 
    else:
        return letter


def letter_is_in(letter, word):
  
    if letter in word:

       
        if letter in guessed_letters:
            print(f'Letter has already entered!!')
            return False

        else:
            return True

    

    else: 
        print(f'"{letter}" is not in the word to guess')
        return False


def print_hangman(tries):
    if tries == 1:
        print(f'''
            _______
            {wrong_letters}
        ''')

    elif tries <= 2:
        print(f'''
             _______
            |/      |
            {wrong_letters}
        ''')

    elif 3 > tries < 5:
        print(f'''
             _______
            |/      |
            |      (_)
            {wrong_letters}
        ''')

    elif 6 > tries < 8:
        print(f'''
         _______
        |/      |
        |      (_)
        |      \|/
        |       |
        {wrong_letters}
        ''')


    else: #tries >= 9:
        print(
    f'''
         _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / /
        |
       _|___
       {wrong_letters}
    '''
    )



word_to_guess = get_word()
first_hint(word_to_guess)
len_word_to_guess = len(word_to_guess)

while len(guessed_letters) != len_word_to_guess:

    letter = ask_for_letter()
    print(f'your attemps: {tries}')

    if letter_is_in(letter, word_to_guess):
        indeces = [index for index, letter_to_compare in enumerate(word_to_guess) if letter == letter_to_compare]
        for index in range(len(indeces)):
            guessed_letters.insert(index, letter)
        print(f"You guessed the letter {letter}!")
        print(guessed_letters)
        

    else:
        wrong_letters.append(letter)
        print_hangman(tries)
        tries += 1

    if len(guessed_letters) == len_word_to_guess:
            print('You win!!!')
            print(word_to_guess)
            break

    if tries > len_word_to_guess -1 :
        print('You loose!!!')
        print(f'the word was: {word_to_guess}')
        break
