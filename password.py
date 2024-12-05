"""
********************************
CS 1026 - Assignment 2 – Password Evaluation
Code by: Arryan Rao
Student ID: arao67
Created on: Oct 8, 2024
********************************
This file implements two key functions: `count_groups` and
`password_strength`. The `count_groups` function assesses the
password to identify the number of different character sets it uses
(lowercase, uppercase, digits, symbols). The `password_strength`
function evaluates and returns the strength of the password based on
its length and character group variety. If any invalid characters
(spaces, tabs, newlines) are found, the password strength is set to 0.
"""

def count_groups(pwd):
    # define allowed character sets
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*/?-+=,.|~"

    # initialize boolean flags for each group
    has_lower = has_upper = has_digit = has_symbol = False
    for char in pwd:
        if char in lower:
            has_lower = True
        elif char in upper:
            has_upper = True
        elif char in digits:
            has_digit = True
        elif char in symbols:
            has_symbol = True
        # ignore characters that are not in these sets, don't return 0

    # return the total number of groups found by summing the boolean values
    return sum([has_lower, has_upper, has_digit, has_symbol])

def password_strength(pwd):
    # check for invalid characters (spaces, tabs, newlines)
    if ' ' in pwd or '\t' in pwd or '\n' in pwd:
        return 0

    # count the number of groups present and return 0 instantly if there are 0
    groups = count_groups(pwd)
    if groups == 0:
        return 0

    # assign password strength based on length and groups
    length = len(pwd)
    if length < 5:
        strength = 0
    elif 5 <= length <= 8:
        if groups <= 1:
            strength = 1
        elif groups <= 3:
            strength = 2
        else:
            strength = 3
    elif 9 <= length <= 12:
        if groups <= 1:
            strength = 2
        elif groups <= 3:
            strength = 3
        else:
            strength = 4
    else:  # length > 12
        if groups <= 1:
            strength = 3
        elif groups <= 3:
            strength = 4
        else:
            strength = 5
    return strength
