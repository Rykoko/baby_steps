import speedtest
import time

speed = speedtest.Speedtest()
loop_count = 0

ds_list = []
us_list = []
ping_list = []


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

    while loop_count < 100:

        print('Loop: ', loop_count + 1)

        ds = speed.download()
        ds_list.append(ds)
        print('\n', 'Download speed: ', humansize(ds), '\n')

        us = speed.upload()
        us_list.append(us)
        print('\n', 'Upload speed: ', humansize(us), '\n')

        servernames = []
        speed.get_servers(servernames)
        ping_list.append(ping_list)
        print('\n', 'Ping:', speed.results.ping, 'ms\n')

        loop_count += 1

        time.sleep(30)

print('loops: ', loop_count)
print(ds_list)
print(us_list)
print(ping_list)

for i in ds_list:
    i += i
    print(i)
    x = i/len(ds_list)
print('Average download speed: ', x)

for j in us_list:
    j += j
    print(j)
    y = j/len(ds_list)
print('Average upload speed: ', y)

for l in ping_list:
    l += l
    print(l)
    z = l/len(ds_list)
print('Average ping: ', z)
