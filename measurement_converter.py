# Convert temperature, speed, distance, weight and area
# Ask what they want to Convert
# Have a function for each field
# Offer two input fields and convert to opposite chosen

import time

# input options
temp_list = ['temp', 'temperature', 'Temp', 'Temperature']
speed_list = ['speed', 'Speed', 'velocity', 'Velocity']
dis_list = ['distance', 'Distance', 'd', 'D', 'dist', 'Dist']
weight_list = ['weight', 'Weight', 'w', 'W']
area_list = ['area', 'Area', 'a', 'A', 'space']

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

# weight variables

kg = 0
KG = ['kg', 'KG', 'ton', 'tons']
lbs = 0
LBS = ['lb', 'lbs']
grams = 0
GRAMS = ['g', 'G', 'Gram', 'Grams', 'gram', 'grams']
oz = 0
OZ = ['ounce', 'oz', 'Oz', 'ounces']
stone = 0
STONE = ['stone', 'st']
ton = 0
TON = ['ton', 'tons', 't', 'T']

# area variables

acre = 0
ACRE = ['acre', 'Acre', 'ac']
hect = 0
HECT = ['hectare', 'Hectare', 'hect', 'Hect']
km2 = 0
KM2 = ['km2', 'KM2', 'Km2', 'kmkm', 'KMKM']
m2 = 0
M2 = ['m2', 'M2', 'meter2', 'Meter2']
mile2 = 0
MILE2 = ['mile2', 'Mile2', 'mi2', 'Mi2', 'milemile', 'MileMile']
y2 = 0
Y2 = ['yard2', 'Yard2', 'yardyard', 'YardYard', 'y2', 'Y2']
f2 = 0
F2 = ['feet2', 'Feet2', 'foot2', 'Foot2',
      'footfoot', 'FootFoot', 'f2', 'F2', 'FF', 'ff']
in2 = 0
IN2 = ['in2', 'In2', 'inch2', 'Inch2', 'inin', 'InIn']


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
    elif convert in weight_list:
        x = input(
            'What are you converting from (kg, grams, lbs, oz, ton, stone)?  ')
        print('')
        y = input('Insert value to be converted: ')
        print('')
    elif convert in area_list:
        x = input(
            'What are you converting from (acre, hectare, km2, m2, miles2, yard2, foot2, inch2)?  ')
        print('')
        y = input('Insert value to be converted: ')
        print('')

    # if value inputted is celcius
    if x in CELCIUS:
        C = float(y)
        print('Fahrenheit: ', format(round((C*1.8)+32, 2)))
        print('Kelvin: ', format(round(C + 273.15, 2)))
        print('')

    # if value inputted is fahrenheit
    elif x in FAHRENHEIT:
        F = float(y)
        print('Celcius: ', format(round((F-32)/1.8, 2)))
        print('Kelvin: ', format(round((F-32 * 5/9)+273.15), str(2)))
        print('')

    # if value inputted is kelvin
    elif x in KELVIN:
        Kelvin = float(y)
        print('Celcius: ', format(round(Kelvin - 273.15, 2)))
        print('Fahrenheit: ', format(
            round((Kelvin - 273.15)*9/5)+32, str(2)))
        print('')

# Converting speed values

    # if value inputted is km/h
    if x in KMH:
        kmh = float(y)
        print('MPH: ', format(round(kmh*0.621371, 4)))
        print('Knots: ', format(round(kmh*0.539957, 4)))
        print('m/s: ', format(round(kmh*0.277778, 4)))
        print('')
    # if value inputted is M/S
    elif x in MS:
        ms = float(y)
        print('Km/h: ', format(round(ms*3.6, 4)))
        print('Knots: ', format(round(ms*1.94384, 4)))
        print('MPH: ', format(round(ms*2.23694, 4)))
        print('')
    # if value inputed is MPH
    elif x in MPH:
        mph = float(y)
        print('Km/h: ', format(round(mph*1.60934, 4)))
        print('Knots: ', format(round(mph*0.868976, 4)))
        print('m/s: ', format(round(mph*0.44704, 4)))
        print('')
    # if value inputted is knots
    elif x in KNOTS:
        kn = float(y)
        print('Km/h: ', format(round(kn*1.852, 4)))
        print('m/s: ', format(round(kn*0.514444, 4)))
        print('MPH: ', format(round(kn*1.15078, 4)))
        print('')

# converting distance values
    # if value is in kilometers
    if x in KM:
        km = float(y)
        print('Miles: ', format(round(km*0.621371, 4)))
        print('Feet: ', format(round(km*3280.84, 4)))
        print('Yards:', format(round(km*1093.61, 4)))
        print('Inches: ', format(round(39370.1, 4)))
        print('Meters: ', format(round(km*1000, 4)))
        print('Centimeters: ', format(round(km*100000, 4)))
        print('')
    # if value is in miles
    elif x in MILES:
        miles = float(y)
        print('Kilometers: ', format(round(miles*1.60934, 4)))
        print('Meters: ', format(round(miles*1609.34, 4)))
        print('Feet: ', format(round(miles*5280, 4)))
        print('Yards:', format(round(miles*1760, 4)))
        print('Inches: ', format(round(miles*63360, 4)))
        print('Centimeters: ', format(round(miles*160934, 4)))
        print('')
    # if value is in meters
    elif x in METERS:
        meters = float(y)
        print('Kilometers: ', format(round(meters*0.001, 4)))
        print('Miles: ', format(round(meters*0.000621371, 4)))
        print('Feet: ', format(round(meters*3.28084, 4)))
        print('Yards:', format(round(meters*1.09361, 4)))
        print('Inches: ', format(round(meters*39.3701, 4)))
        print('Centimeters: ', format(round(meters*100, 4)))
        print('')
    # if value is in feet
    elif x in FEET:
        feet = float(y)
        print('Kilometers: ', format(round(feet*0.0003048, 4)))
        print('Meters: ', format(round(feet*0.3048, 4)))
        print('Miles: ', format(round(feet*0.000189394, 4)))
        print('Yards:', format(round(feet*0.333333, 4)))
        print('Inches: ', format(round(feet*12, 4)))
        print('Centimeters: ', format(round(feet*30.48, 4)))
        print('')
    # if value is in yards
    elif x in YARDS:
        yards = float(y)
        print('Kilometers: ', format(round(yards*0.0009144, 4)))
        print('Meters: ', format(round(yards*0.9144, 4)))
        print('Miles: ', format(round(yards*0.000568182, 4)))
        print('feet:', format(round(yards*3, 4)))
        print('Inches: ', format(round(yards*36, 4)))
        print('Centimeters: ', format(round(yards*91.44, 4)))
        print('')
    # if value is in inches
    elif x in INCHES:
        inches = float(y)
        print('Kilometers: ', format(round(inches*0.0000254, 4)))
        print('Meters: ', format(round(inches*0.0254, 4)))
        print('Miles: ', format(round(inches*0.000015783, 4)))
        print('feet:', format(round(inches*0.0833333, 4)))
        print('Yards: ', format(round(inches*0.0277778, 4)))
        print('Centimeters: ', format(round(inches*2.54, 4)))
        print('')
    # if value is in centimeters
    elif x in CENTIMETERS:
        centimeters = float(y)
        print('Kilometers: ', format(round(centimeters*0.00001, 4)))
        print('Meters: ', format(round(centimeters*0.01, 4)))
        print('Miles: ', format(round(centimeters*0.0000062137, 4)))
        print('feet:', format(round(centimeters*0.0328084, 4)))
        print('Yards: ', format(round(centimeters*0.0109361, 4)))
        print('inches: ', format(round(centimeters*0.393701, 4)))
        print('')

# converting weight values
    # if values is in KG
    if x in KG:
        kg = float(y)
        print('Grams: ', format(round(kg*1000, 4)))
        print('Ton: ', format(round(kg*0.000984207, 4)))
        print('Ounces: ', format(round(35.274, 4)))
        print('Stone: ', format(round(0.157473, 4)))
        print('Pounds: ', format(round(kg*2.20462, 4)))
        print('')
    # if value is in grams
    elif x in GRAMS:
        grams = float(y)
        print('Kilograms: ', format(round(grams*0.001, 4)))
        print('Ton: ', format(round(grams*0.00000098421, 4)))
        print('Ounces: ', format(round(grams*0.035274, 4)))
        print('Stone: ', format(round(grams*0.000157473, 4)))
        print('Pounds: ', format(round(grams*0.00220462, 4)))
        print('')
    # if value is in ton
    elif x in TON:
        ton = float(y)
        print('Kilograms: ', format(round(ton*1016.05, 4)))
        print('Grams: ', format(round(ton*101600000, 4)))
        print('Ounces: ', format(round(ton*35840, 4)))
        print('Stone: ', format(round(ton*160, 4)))
        print('Pounds: ', format(round(ton*2240, 4)))
        print('')
    # if value is in Oz
    elif x in OZ:
        oz = float(y)
        print('Kilograms: ', format(round(oz*0.0283495, 4)))
        print('Grams: ', format(round(oz*28.3495, 4)))
        print('Ton: ', format(round(oz*0.000027902, 4)))
        print('Stone: ', format(round(oz*0.00446429, 4)))
        print('Pounds: ', format(round(oz*0.0625, 4)))
        print('')
    # if value is in stone
    elif x in STONE:
        stone = float(y)
        print('Kilograms: ', format(round(stone*6.35029, 4)))
        print('Grams: ', format(round(stone*6350.29, 4)))
        print('Ton: ', format(round(stone*0.00625, 4)))
        print('Ounces: ', format(round(stone*224, 4)))
        print('Pounds: ', format(round(stone*14, 4)))
        print('')
    # if value is in lbs
    elif x in LBS:
        lbs = float(y)
        print('Kilograms: ', format(round(lbs*0.453592, 4)))
        print('Grams: ', format(round(lbs*453.592, 4)))
        print('Ton: ', format(round(lbs*0.000446329, 4)))
        print('Ounces: ', format(round(lbs*16, 4)))
        print('Stone: ', format(round(lbs*0.0714286, 4)))
        print('')

# *** === TESTED AND WORKS TO HERE === ***

# converting area values
    # if value is in km2
    if x in KM2:
        km = float(y)
        print(f'Meters\N{SUPERSCRIPT TWO}: ', format(round(km2*1000000, 4)))
        print(f'Miles\N{SUPERSCRIPT TWO}: ', format(round(km2*0.386102, 4)))
        print(f'Yards\N{SUPERSCRIPT TWO}: ', format(round(km2*0.000001196, 4)))
        print(f'Feet\N{SUPERSCRIPT TWO}: ', format(round(km2*0.0000001076, 4)))
        print(f'Inches\N{SUPERSCRIPT TWO}: ',
              format(round(km2*0.00000000155, 4)))
        print('Acres: ', format(round(km2*247.105, 4)))
        print('Hectares: ', format(round(km2*100, 4)))
    # if value is in m2
    elif x in M2:
        m2 = float(y)
        print(f'Kilometers\N{SUPERSCRIPT TWO}: ',
              format(round(m2*0.000001, 4)))
        print(f'Miles\N{SUPERSCRIPT TWO}: ', format(round(m2*0.0000003861, 4)))
        print(f'Yards\N{SUPERSCRIPT TWO}: ', format(round(m2*1.19599, 4)))
        print(f'Feet\N{SUPERSCRIPT TWO}: ', format(round(m2*10.7639, 4)))
        print(f'Inches\N{SUPERSCRIPT TWO}: ', format(round(m2*1550, 4)))
        print('Acres: ', format(round(m2*0.000247105, 4)))
        print('Hectares: ', format(round(m2*0.0001, 4)))
    # if value is in mile2
    elif x in MILE2:
        mile2 = float(y)
        print(f'Kilometers\N{SUPERSCRIPT TWO}: ',
              format(round(mile2*2.58999, 4)))
        print(f'Meters\N{SUPERSCRIPT TWO}: ', format(round(mile2*2590000, 4)))
        print(f'Yards\N{SUPERSCRIPT TWO}: ', format(round(mile2*3098000, 4)))
        print(f'Feet\N{SUPERSCRIPT TWO}: ', format(round(mile2*2.7880000, 4)))
        print(f'Inches\N{SUPERSCRIPT TWO}: ',
              format(round(mile2*4014000000, 4)))
        print('Acres: ', format(round(mile2*640, 4)))
        print('Hectares: ', format(round(mile2*258.99, 4)))
    # if value is in acres
    elif x in ACRE:
        acre = float(y)
        print(f'Kilometers\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Meters\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Miles\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Yards\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Feet\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Inches\N{SUPERSCRIPT TWO}: ', format(round()))
        print('Acres: ', format(round()))
        print('Hectares: ', format(round()))
    # if value is in hectares
    elif x in HECT:
        hect = float(y)
        print(f'Kilometers\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Meters\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Miles\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Yards\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Feet\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Inches\N{SUPERSCRIPT TWO}: ', format(round()))
        print('Acres: ', format(round()))
        print('Hectares: ', format(round()))
    # if value is in yards2
    elif x in Y2:
        y2 = float(y)
        print(f'Kilometers\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Meters\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Miles\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Yards\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Feet\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Inches\N{SUPERSCRIPT TWO}: ', format(round()))
        print('Acres: ', format(round()))
        print('Hectares: ', format(round()))
    # if value is in feet2
    elif x in F2:
        f2 = float(y)
        print(f'Kilometers\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Meters\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Miles\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Yards\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Feet\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Inches\N{SUPERSCRIPT TWO}: ', format(round()))
        print('Acres: ', format(round()))
        print('Hectares: ', format(round()))
    # if value is in inches2
    elif x in IN2:
        in2 = float(y)
        print(f'Kilometers\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Meters\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Miles\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Yards\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Feet\N{SUPERSCRIPT TWO}: ', format(round()))
        print(f'Inches\N{SUPERSCRIPT TWO}: ', format(round()))
        print('Acres: ', format(round()))
        print('Hectares: ', format(round()))


declaring()
