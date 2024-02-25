#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def computer_guess():
    max_num = int(input("Enter the maximum number: "))
    number = int(input(f"Think of a number between 1 and {max_num}: "))
    low = 1
    high = max_num
    attempts = 0

    while low <= high:
        guess = random.randint(low, high)
        print(f"The computer guesses: {guess}")
        attempts += 1

        if guess == number:
            print(f'Yay! The computer guessed your number, {guess}, correctly in {attempts} attempts!')
            break
        elif guess < number:
            print('Too low.')
            low = guess + 1
        else:
            print('Too high.')
            high = guess - 1

def main():
    print("Welcome to the Guessing Game!")
    computer_guess()

if __name__ == "__main__":
    main()


# In[ ]:




