import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.list_of_guesses = []
        self.num_letters = len(set(self.word))

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for word_id in range(len(self.word)):
                if guess == self.word[word_id]:
                    self.word_guessed[word_id] = guess
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = input("Please choose a single alphabetical character:")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                break


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list , num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            print(game.num_lives)
            print(game.num_letters)
            print(game.list_of_guesses)
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break
        
word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']

play_game(word_list)