# Create QR codes using python

import time
import random
from random import choice

# Take user input

intro = print(
    'What words or numbers would you like to use, \nyou will be asked for three seperate inputs:\n\n')
time.sleep(2)

entry1 = input('First Word or Number: ')
entry2 = input('Second Word or Number: ')
entry3 = input('Third Word or Number: ')

# Add values into one string

characters = (entry1 + entry2 + entry3)

# Mix the string between upper and lowercase characters

mix = ''.join(choice((str.upper, str.lower))(char) for char in characters)

# Length of characters for percentage

len_chars = len(characters)
per_chars = (int((len_chars/100)*70))

# Generate password

password = ''

for c in range(per_chars):
    password += random.choice(mix)

# Print it!

print('Generating password...')
time.sleep(1)

print("\n\n", password, "\n\n")
