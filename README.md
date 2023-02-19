# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 2

* Task 1: adds *word_list* variable with a list of fruits
* Task 2: adds *word* variable which randomly chooses a fruit from *word_list*
* Task 3: adds *guess* variable whcih asks user to choose a letter
* Task 4: adds if statement to check if *guess* variable is an alphabetical letter and not more than one symbol is in input 

## Milestone 3

* Task 1: adds while loop to keep checking *guess* input until it is correct
* Task 2: adds if statement to check if *guess* input matches any letter from *word* variable
* Task 3: separates previous code into two separate functions *check guess* and *ask_for_input*.
  * *ask_for_input* verifies user input and passes variable *guess* to the *check_guess* function to check if letter from variable *guess* is in the *word*

## Milestone 4

* Task 1: creates a class Hangman with 2 parameters word_list and num_lives
 
 **Parameters**
  * word_list: list
        List of words to be used in the game
  * num_lives: int
        Number of lives the player has
        
**Attributes**
  * word: str
        The word to be guessed picked randomly from the word_list
  * word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
  * num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
  * num_lives: int
        The number of lives the player has
  * list_letters: list
        A list of the letters that have already been tried
        
* Task 2 : creates *check_letter* and *ask_letter* methods
  * check_letter(letter)
        Checks if letter is in the word
  * ask_letter()
        Asks user for a letter
        
* Task 3: defines what happens if letter is in the word
  * replaces the underscore(s) in the word_guessed with the letter guessed by the user.

* Task 4: defines what happens if the guess is not in the word you are trying to guess.
  * reduces *num_lives* by 1.
  * prints a message saying "Sorry, {letter} is not in the word."
  * prints another message saying "You have {num_lives} lives left."



