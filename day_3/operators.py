# Day 3: 30 Days of python programming
"""
# OPERATORS:
(a) Assignment Operators: used to assign values to variables.
    ==
    =
    +
    -
    &=
    |=

(b) Arithmetic Operators:
    Addition(+): a + b
    Subtraction(-): a - b
    Multiplication(*): a * b
    Division(/): a / b
    Modulus(%): a % b
    Floor division(//): a // b
    Exponentiation(**): a ** b

(c) Comparison Operators: Used to  to compare two values
    == Equal
    != Not Equal
    >  Greater Than
    <  Less Than
    >= Greater than or Equal To
    <= Less Than or Equal To

(d) Logical Operators: Used to combine conditional statements:
    and - Returns True if both statements are true
    or  - Returns True if one of the statements is true
    not - Returns false if the result is true

"""
print('Addition: ', 44 + 45)        # 96
print('Subtraction: ', 45 - 35)     # 10
print('Multiplication: ', 10 * 3)   # 30
print ('Division: ', 44 / 5)        # 8.8  Division in Python gives floating number
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2

# Comparison Operators
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

#Logical Operators
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False