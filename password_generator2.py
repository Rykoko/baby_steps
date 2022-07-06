# Create QR codes using python

import time
import random

# Function for string slicing


def slice(string):
    list1 = []
    list1[0:] = string
    return list1

# Take user input


intro = print(
    'What words or numbers would you like to use, \nyou will be asked for three seperate inputs:\n\n')
time.sleep(2)

entry1 = input('First Word or Number: ')
entry2 = input('Second Word or Number: ')
entry3 = input('Third Word or Number: ')

# Add values into one string

characters = (entry1 + entry2 + entry3)

# Length of characters for percentage

len_chars = len(characters)
per_chars = (int((len_chars/100)*70))

# Make list of individual characters

slice_list = slice(characters)

# Generate password

password = ''

for c in range(per_chars):
    password += random.choice(characters)

print(password)
