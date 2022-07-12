import speedtest
import time

speed = speedtest.Speedtest()
loop_count = 0

# lists to store data speeds

ds_list = []
us_list = []

# function to demonstrate numbers in correct format


def humansize(nbits):
    suffixes = ['b/s', 'Kb/s', 'Mbit/s', 'Gb/s', 'Tb/s', 'Pb/s']
    i = 0
    while nbits >= 1024 and i < len(suffixes)-1:
        nbits /= 1024.
        i += 1
    f = ('%.2f' % nbits).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

# loop to go through speeds


entry = input('Hit enter to run test')
if len(entry) < 1:

    while loop_count < 5:  # this is the number of times program will loop

        print('Loop: ', loop_count + 1)

        # check download speed

        ds = speed.download()
        ds_list.append(ds)
        print('\n', 'Download speed: ', humansize(ds), '\n')

        # check upload speeds

        us = speed.upload()
        us_list.append(us)
        print('\n', 'Upload speed: ', humansize(us), '\n')

        loop_count += 1

        # time to elapse between loops

        time.sleep(300)

print('Loops completed: ', loop_count, '\n')

# if you want to view lists (in bits) you can un-hash below

# print(ds_list)
# print(us_list)

# calculate average and compensate for correct values

x = float(round(sum(ds_list)/len(ds_list), 2))
x2 = humansize(x)
print('Average download speed: ', x2)
y = float(round(sum(us_list)/len(us_list), 2))
y2 = humansize(y)
print('Average upload speed: ', y2, '\n')
