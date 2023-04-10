# Introduction
# Day 2 - 30DaysOfPython Challenge
"""
    VARIABLES: Container of some value inside your computer memory.
"""
# Ask user name and say hello to user

name = input("What is yout name? ")
name = name.strip().title() # Remove whitespace from str & capitalize user names

print(f"Hello, {name}")

# Declaring Multiple Variable in a Line

car_model, car_type, car_country, age, over_10 = "Toyota Hilux", "Pickup", "Japan", 9, False 

print("Car model: ", car_model)
print("Car type: ", car_type)
print("Country of origin: ", car_country)
print("Age: ", age)
print("Over 10 years: ", over_10)