"""
==Strings==
-Any data type written as text is a string.
-Any data under single, double or triple quote are strings.
-There are different string methods and built-in functions to deal with string data types.
-To check the length of a string use the len() method.
"""
#1. CREATING A STRING ('')
letter = 'G'                # A string could be a single character or a bunch of texts
print(letter)               # G
print(len(letter))          # 1
greeting = 'Hello, Techies!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 15
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

#2. CREATING A MULTILINE STRING (''' or """)
multiline_string = '''I am a techie and enjoy coding.
I believe tech can and will change my life drastically.
That is why I am always coding and partaking in 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a techie and enjoy coding.
I believe tech can and will change my life drastically.
That is why I am always coding and partaking in 30 days of python."""
print(multiline_string)

#3. String Concatenation:  Merging or connecting strings is called concatenation
first_name = 'Happy '
last_name = 'Techie'
full_name = first_name  + last_name
print(full_name) # Happy Techie
# Checking the length of a string using len() built-in function
print(len(first_name))  # 6
print(len(last_name))   # 6
print(len(first_name) > len(last_name)) # False
print(len(full_name)) # 12

#4. Escape Sequences in Strings
'''In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
'''
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote
