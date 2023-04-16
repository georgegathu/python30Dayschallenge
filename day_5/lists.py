"""
LISTS IN PYTHON:
There are four collection data types in Python :

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

    # syntax
    lst = []
"""
#Lets Create a List:
cars = ["Toyota", "Ford", "Isuzu", "Nisan"]                          # list of cars
dogs = ['Doberman', 'Rottweiler','Pit Bull','Rottweiler', 'Mutina']  # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']              # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Node', 'Php', 'MongDB']   # list of web technologies
countries = ['Kenya', 'Tanzania', 'Uganda', 'Nigeria', 'Ghana']      # list of countries

# Print the lists and its length
print("Ford:", cars)
print('Number of cars:', len(cars))
print('dogs:', dogs)
print('Number of dogs:', len(dogs))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
