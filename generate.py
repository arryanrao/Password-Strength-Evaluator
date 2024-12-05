"""
********************************
CS 1026 - Assignment 2 – Password Evaluation
Code by: Arryan Rao
Student ID: arao67
Created on: Oct 8, 2024
********************************
This file defines a function `generate_password`, which creates a random
password of a specified length. Characters for the password are selected
randomly from four defined groups (lowercase, uppercase, digits, and symbols),
using Python's `random.choice` function. The function returns the final
randomly constructed password.
"""
import random

def generate_password(length):
    ALL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*/?-+=,.|~"
    pwd = ""
    for i in range(length): # run through the loop and keep adding random characters to the string until desired length
        temp = random.choice(ALL_CHARS)
        pwd = temp + pwd
    return pwd
