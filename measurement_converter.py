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

def declaring():
    convert = input(
        "What would you like to convert (speed, temp, area, distance, weight)? ")
    if convert in temp_list:
        x = input('What are you converting from (celcius, fahrenheit, kelvin)? ')
        print('')
        y = input('Insert value to be converted: ')
        print('')
    elif convert in speed_list:
        x = input('What are you converting from (km/h, mph, m/s, kn)?  ')
        print('')
        y = input('Insert value to be converted: ')
        print('')
    elif convert in dis_list:
        x = input(
            'What are you converting from (km, miles, feet, meters, inches, centimeters, yards)?  ')
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

# converting distance values
    # if value is in kilometers
    if x in KM:
        km = int(y)
        print('Miles: ', round(km*0.621371))
        print('Feet: ', round(km*3280.84))
        print('Yards:', round(km*1093.61))
        print('Inches: ', round(39370.1))
        print('Meters: ', round(km*1000))
        print('Centimeters: ', round(km*100000))
        print('')
    # if value is in miles
    elif x in MILES:
        miles = int(y)
        print('Kilometers: ', round(miles*1.60934))
        print('Meters: ', round(miles*1609.34))
        print('Feet: ', round(miles*5280))
        print('Yards:', round(miles*1760))
        print('Inches: ', round(miles*63360))
        print('Centimeters: ', round(miles*160934))
        print('')
    # if value is in meters
    elif x in METERS:
        meters = int(y)
        print('Kilometers: ', round(meters*0.001))
        print('Miles: ', round(meters*0.000621371))
        print('Feet: ', round(meters*3.28084))
        print('Yards:', round(meters*1.09361))
        print('Inches: ', round(meters*39.3701))
        print('Centimeters: ', round(meters*100))
        print('')
    # if value is in feet
    elif x in FEET:
        feet = int(y)
        print('Kilometers: ', round(feet*0.0003048))
        print('Meters: ', round(feet*0.3048))
        print('Miles: ', round(feet*0.000189394))
        print('Yards:', round(feet*0.333333))
        print('Inches: ', round(feet*12))
        print('Centimeters: ', round(feet*30.48))
        print('')
    # if value is in yards
    elif x in YARDS:
        yards = int(y)
        print('Kilometers: ', round(yards*0.0009144))
        print('Meters: ', round(yards*0.9144))
        print('Miles: ', round(yards*0.000568182))
        print('feet:', round(yards*3))
        print('Inches: ', round(yards*36))
        print('Centimeters: ', round(yards*91.44))
        print('')
    # if value is in inches
    elif x in INCHES:
        inches = int(y)
        print('Kilometers: ', round(inches*0.0000254))
        print('Meters: ', round(inches*0.0254))
        print('Miles: ', round(inches*0.000015783))
        print('feet:', round(inches*0.0833333))
        print('Yards: ', round(inches*0.0277778))
        print('Centimeters: ', round(inches*2.54))
        print('')
    elif x in CENTIMETERS:
        centimeters = int(y)
        print('Kilometers: ', round(centimeters*0.00001))
        print('Meters: ', round(centimeters*0.01))
        print('Miles: ', round(centimeters*0.0000062137))
        print('feet:', round(centimeters*0.0328084))
        print('Yards: ', round(centimeters*0.0109361))
        print('inches: ', round(centimeters*0.393701))
        print('')

    

declaring()
