# create random sequence of characters

import random
import time

print('===PASSWORD GENERATOR===')

characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!"£$%&/()=?^<>-_,.;:@#*+{}[]\|"'

length = input('Enter desired length of password: ')
length = int(length)

print('\nGenerating Password...\n')
time.sleep(1.0)
print('\nPassword ---> \n')

password = ''

for c in range(length):
    password += random.choice(characters)

print(' \n', password, '\n')
