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