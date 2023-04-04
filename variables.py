# Introduction
# Day 2 - 30DaysOfPython Challenge
"""
    VARIABLES: Container of some value inside your computer memory.
"""
# Ask user name and say hello to user

name = input("What is yout name? ")
name = name.strip().title() # Remove whitespace from str & capitalize user names

print(f"Hello, {name}")