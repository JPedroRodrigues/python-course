from time import sleep
print('CLOCK RUNNING DOWN...')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('SHOT CLOCK VIOLATION')
