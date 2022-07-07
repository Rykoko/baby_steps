# Convert temperature, speed, distance, weight and area
# Ask what they want to Convert
# Have a function for each field
# Offer two input fields and convert to opposite chosen

# temp variables
C = 0
F = 0
Kelvin = 0

# speed variables
kmh = 0
mph = 0
kn = 0
ms = 0

convert = input(
    "What would you like to convert (speed, temp, area, distance, weight)? ")


# Converting temperature values
if convert == ('temp' or 'temperature' or 'Temp' or 'Temperature'):
    x = input('What are you converting from (celcius, fahrenheit, kelvin)? ')
    y = input('Insert value to be converted: ')

    # if value inputted is celcius
    if x == ('c' or 'C' or 'Celcius' or 'celcius'):
        C = int(y)
        print('Fahrenheit: ', round(((C*1.8)+32)))
        print('Kelvin: ', round((C + 273.15)))

    # if value inputted is fahrenheit
    elif x == ('f' or 'Fahrenheit' or 'fahrenheit'):
        F = int(y)
        print('Celcius: ', round(((F-32)/1.8)))
        print('Kelvin: ', round((((F-32)*5)/9)+273.15))

    # if value inputted is kelvin
    elif x == ('k' or 'K' or 'kelvin' or 'Kelvin'):
        Kelvin = int(y)
        print('Celcius: ', round((Kelvin - 273.15)))
        print('Fahrenheit: ', round(((Kelvin - 273.15)*9)/5)+32)

# Converting speed values
elif convert == ('speed' or 'Speed' or 'velocity' or 'Velocity'):
    x = input('What are you converting from (km/h, mph, m/s, kn)? ')
    y = input('Insert value to be converted: ')

    # if value inputted is km/h
    if x == ('km/h' or 'KM/H' or 'Km/h' or 'Km/H' or 'kmh'):
        kmh = int(y)
        print('MPH: ', round((kmh*0.621371)))
        print('Kn: ', round((kmh*0.539957)))
        print('m/s: ', round((kmh*0.277778)))
    # if value inputed is MPH
    elif x == ('mph' or 'MPH' or 'MpH'):
        mph = int(y)
        print('Km/h: ', round(mph*1.60934))
        print('Kn: ', round(mph*0.868976))
        print('m/s: ', round(mph*0.44704))
    # if value inputted is M/S
    elif x == ('m/s' or 'ms' or 'MS' or 'M/S' or 'M/s'):
        ms = int(y)
        print('Km/h: ', round(ms*3.6))
        print('Kn: ', round(ms*1.94384))
        print('MPH: ', round(ms*2.23694))
    # if value inputted is knots
    elif x == ('kn' or 'KN' or 'knots' or 'KNOTS' or 'Knots'):
        kn = int(y)
        print('Km/h: ', round(kn*1.852))
        print('m/s: ', round(kn*0.514444))
        print('MPH: ', round(kn*1.15078))
