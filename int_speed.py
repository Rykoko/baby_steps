import speedtest
import time

speed = speedtest.Speedtest()


def humansize(nbits):
    suffixes = ['b/s', 'Kb/s', 'Mbit/s', 'Gb/s', 'Tb/s', 'Pb/s']
    i = 0
    while nbits >= 1024 and i < len(suffixes)-1:
        nbits /= 1024.
        i += 1
    f = ('%.2f' % nbits).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


entry = int(input(
    '''Test options --> \n\n 1) Download Speed \n 2) Upload Speed \n 3) Ping \n
            4) To quit program \n\n Select a number to test: '''))

while True:

    if entry == 1:
        print('\nTesting download speed...')
        ds = speed.download()
        print('\n', 'Download speed: ', humansize(ds), '\n')
    elif entry == 2:
        print('\nTesting upload speed...')
        us = speed.upload()
        print('\n', 'Upload speed: ', humansize(us), '\n')
    elif entry == 3:
        print('\nChecking da ping ping yo...')
        servernames = []
        speed.get_servers(servernames)
        print('\n', 'Ping:', speed.results.ping, 'ms\n')
    elif entry == 4:
        print('\nquitting...\n')
        time.sleep(1)
        quit()
    else:
        print('\nPlease enter a valid number\n')
        
    retry = int(input('Select a number: '))
    entry = retry
