# Convert temperature, speed, distance, weight and area
# Ask what they want to Convert
# Have a function for each field
# Offer two input fields and convert to opposite chosen

C = 0
F = 0
Kelvin = 0

convert = input(
    "What would you like to convert (speed, temp, area, distance, weight)? ")


if convert == ('temp' or 'temperature' or 'Temp' or 'Temperature'):
    x = input('What are you converting from (celcius, fahrenheit, kelvin)? ')
    y = input('Insert value to be converted: ')
    if x == ('c' or 'C' or 'Celcius' or 'celcius'):
        C = int(y)
        print('Fahrenheit: ', int(((C*1.8)+32)))
        print('Kelvin: ', int((C + 273.15)))
    elif x == ('f' or 'Fahrenheit' or 'fahrenheit'):
        F = int(y)
        print('Celcius: ', int(((F-32)/1.8)))
        print('Kelvin: ', int((((F-32)*5)/9)+273.15))
    elif x == ('k' or 'K' or 'kelvin' or 'Kelvin'):
        Kelvin = int(y)
        print('Celcius: ', int((Kelvin - 273.15)))
        print('Fahrenheit: ', int(((Kelvin - 273.15)*9)/5)+32)
elif convert == ('speed' or 'Speed' or 'velocity' or 'Velocity'):
    x = input('What are you converting from (km/h, mph, m/s, kn)? ')
    y = input('Insert value to be converted: ')

    # def temperature():
    #     if convert = 'temp' or 'temperature':
    #         F = ((C*1.8)+32)
