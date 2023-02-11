while True:
    guess = input('Please choose a single letter:')
    if len(guess) == 1 and guess.isalpha():
        print('Goog guess!')
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')