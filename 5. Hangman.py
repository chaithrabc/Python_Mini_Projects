#!/usr/bin/env python
# coding: utf-8

# In[2]:


def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter only one letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter.")
        else:
            return guess

def play_hangman(word):
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
        else:
            print("Correct guess!")
        
        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)

        if '_' not in displayed_word:
            print("Congratulations! You guessed the word.")
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    word = input("Player 1, please enter a word: ").lower()
    play_hangman(word)


# In[ ]:




