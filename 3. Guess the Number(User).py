#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

def guess_game():
    max_num = int(input("Enter the maximum number: "))
    random_number = random.randint(1, max_num)
    attempts = 0

    while True:
        guess = int(input(f'Guess a number between 1 and {max_num}: '))
        attempts += 1

        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        else:
            print(f'Yay, congrats. You have guessed the number {random_number} correctly in {attempts} attempts!!')
            break

def main():
    print("Welcome to the Guessing Game!")
    guess_game()

if __name__ == "__main__":
    main()


# In[ ]:




