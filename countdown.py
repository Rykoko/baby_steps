import time

countdown = input('Insert countdown time in seconds: ')
count = int(countdown)
while count >= 1:
    time.sleep(1)
    count = count - 1
    print(count)
    if count == 1:
        break
time.sleep(1)
print('blastoff!')
