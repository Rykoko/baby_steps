import speedtest
import time

speed = speedtest.Speedtest()

entry = int(input(
    '''Test options --> \n\n 1) Download Speed \n 2) Upload Speed \n 3) Ping \n 4) To quit program \n\n Select a number to test: '''))

while True:

    if entry == 1:
        print('\n', 'Download speed:', speed.download(), '\n')
    elif entry == 2:
        print('\n', 'Upload speed:', speed.upload(), '\n')
    elif entry == 3:
        servernames = []
        speed.get_servers(servernames)
        print('\n', 'Ping:', speed.results.ping, '\n')
    elif entry == 4:
        print('\nquitting...\n')
        time.sleep(1)
        quit()
    else:
        print('\nPlease enter a valid number\n')
    retry = int(input('Select a number: '))
    entry = retry
