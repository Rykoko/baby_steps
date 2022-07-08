# Convert temperature, speed, distance, weight and area
# Ask what they want to Convert
# Have a function for each field
# Offer two input fields and convert to opposite chosen

import time

# input options
temp_list = ['temp', 'temperature', 'Temp', 'Temperature']
speed_list = ['speed', 'Speed', 'velocity', 'Velocity']
dis_list = ['distance', 'Distance', 'd', 'D', 'dist', 'Dist']
weight_list = []
area_list = []

# temp variables
C = 0
CELCIUS = ['c', 'C', 'Celcius', 'celcius']
F = 0
FAHRENHEIT = ['f', 'Fahrenheit', 'fahrenheit']
Kelvin = 0
KELVIN = ['k', 'K', 'kelvin', 'Kelvin']

# speed variables
kmh = 0
KMH = ['kmh', 'Km/h', 'KM/H', 'Km/H', 'km/h']
mph = 0
MPH = ['mph', 'MPH', 'MpH']
kn = 0
KNOTS = ['kn', 'KN', 'knots', 'KNOTS', 'Knots']
ms = 0
MS = ['m/s', 'ms', 'MS', 'M/S', 'M/s']

# distance variables

km = 0
KM = ['km', 'KM', 'kilometers', 'Kilometers']
miles = 0
MILES = ['Miles', 'miles']
feet = 0
FEET = ['Foot', 'foot', 'feet', 'foots', '"']
meters = 0
METERS = ['m', 'meters', 'Meters']
inches = 0
INCHES = ['inches', "'", 'inch', 'Inch', 'Inches']
centimeters = 0
CENTIMETERS = ['cm', 'cms', 'CM', 'CMs', 'centimeters', 'Centimeters']
yards = 0
YARDS = ['yard', 'yards', 'where is the wall?']

convert = input(
    "What would you like to convert (speed, temp, area, distance, weight)? ")


# Converting temperature values
if convert in temp_list:
    x = input('What are you converting from (celcius, fahrenheit, kelvin)? ')
    print('')
    y = input('Insert value to be converted: ')
    print('')

    # if value inputted is celcius
    if x in CELCIUS:
        C = int(y)
        print('Fahrenheit: ', round(((C*1.8)+32)))
        print('Kelvin: ', round((C + 273.15)))
        print('')

    # if value inputted is fahrenheit
    elif x in FAHRENHEIT:
        F = int(y)
        print('Celcius: ', round(((F-32)/1.8)))
        print('Kelvin: ', round((((F-32)*5)/9)+273.15))
        print('')

    # if value inputted is kelvin
    elif x in KELVIN:
        Kelvin = int(y)
        print('Celcius: ', round((Kelvin - 273.15)))
        print('Fahrenheit: ', round(((Kelvin - 273.15)*9)/5)+32)
        print('')

# Converting speed values
elif convert in speed_list:
    x = input('What are you converting from (km/h, mph, m/s, kn)?  ')
    print('')
    y = input('Insert value to be converted: ')
    print('')

    # if value inputted is km/h
    if x in KMH:
        kmh = int(y)
        print('MPH: ', round((kmh*0.621371)))
        print('Knots: ', round((kmh*0.539957)))
        print('m/s: ', round((kmh*0.277778)))
        print('')
        # if value inputted is M/S
    elif x in MS:
        ms = int(y)
        print('Km/h: ', round(ms*3.6))
        print('Knots: ', round(ms*1.94384))
        print('MPH: ', round(ms*2.23694))
        print('')
    # if value inputed is MPH
    elif x in MPH:
        mph = int(y)
        print('Km/h: ', round(mph*1.60934))
        print('Knots: ', round(mph*0.868976))
        print('m/s: ', round(mph*0.44704))
        print('')
    # if value inputted is knots
    elif x in KNOTS:
        kn = int(y)
        print('Km/h: ', round(kn*1.852))
        print('m/s: ', round(kn*0.514444))
        print('MPH: ', round(kn*1.15078))
        print('')

elif convert in dis_list:
    x = input(
        'What are you converting from (km, miles, feet, meters, inches, centimeters, yards)?  ')
    print('')
    y = input('Insert value to be converted: ')
    print('')
    if x in dis_list:
        km = int(y)
        print('Miles: ', round())
        print('Feet: ', round())
        print('Yards:', round())
        print('Meters: ', round())
        print('Kilometers: ', round())
        print('Inches: ', round())
