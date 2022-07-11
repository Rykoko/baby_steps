import speedtest
import time

speed = speedtest.Speedtest()
loop_count = 0


def humansize(nbits):
    suffixes = ['b/s', 'Kb/s', 'Mbit/s', 'Gb/s', 'Tb/s', 'Pb/s']
    i = 0
    while nbits >= 1024 and i < len(suffixes)-1:
        nbits /= 1024.
        i += 1
    f = ('%.2f' % nbits).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


entry = input('Hit enter to run test')
if len(entry) < 1:

    while loop_count < 2:

        print('Loop: ', loop_count + 1)

        ds = speed.download()
        print('\n', 'Download speed: ', humansize(ds), '\n')

        us = speed.upload()
        print('\n', 'Upload speed: ', humansize(us), '\n')

        servernames = []
        speed.get_servers(servernames)
        print('\n', 'Ping:', speed.results.ping, 'ms\n')

        loop_count += 1

        time.sleep(30)

print('loops: ', loop_count)
