"""
********************************
CS 1026 - Assignment 2 – Password Evaluation
Code by: Arryan Rao
Student ID: arao67
Created on: Oct 8, 2024
********************************
This file contains the `process_password` function, which interacts
with the user to either accept an inputted password or generate one.
The loop continues until the password meets or exceeds the required
strength threshold. This script imports necessary functions from
password.py and generate.py to handle password checking and
generation tasks.
"""

from password import *
from generate import *

def process_password(min_strength):
    while True:
        user_input = input("Type in a new password or type X for a randomly generated password: ")

        # check if the user wants a randomly generated password
        if user_input.lower() == 'x':
            password = generate_password(15)  # generate a 15-character password and end the program since it works
            print(f"Your password: {password}")
            print("Your password is strong enough! Thank you.")
            break
        else:
            password = user_input
            print(f"You entered: {password}")

        # check and display password strength
        strength = password_strength(password)
        print(f"Your password has a strength of {strength}")

        # compare the password's strength with the required minimum strength
        # if it's strong enough, break the loop and end the program. else: retry
        if strength >= min_strength:
            print("Your password is strong enough! Thank you.")
            break
        else:
            print("Your password is not strong enough. Please create a new password that is stronger.")
