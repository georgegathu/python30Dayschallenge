# SETS
"""
    -Set: Set is a collection of items.
    -Set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
    -Creating a Set:
    We use curly brackets, {} to create a set or the set() built-in function.
    =empty set:
    # syntax
        st = {}
        # or
        st = set()
    -A set example:
    fruits = {'banana', 'orange', 'melon', 'lemon'}
"""
# Getting Set's Length
# We use len() method to find the length of a set.
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
print(len(fruits))


# Accessing Items in a Set
# We use loops to access items. We will see this in loop section
# Exmample: To check if an item exist in a list we use in membership operator.
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True