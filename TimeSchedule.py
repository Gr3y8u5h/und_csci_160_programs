# loop that counts from 9:00 to 4:00 in 15 minutes increments

TIME_FRAME = 20  # Capitilize named constants

for hour in range(9, 12 + 1, 1):
    for minute in range(0, 60, TIME_FRAME):
        print(format(hour, '2d'), ':', format(minute, '02d'), sep='')

for hour in range(1, 3 + 1, 1):
    for minute in range(0, 60, TIME_FRAME):
        print(format(hour, '2d'), ':', format(minute, '02d'), sep='')

hour = 4
minute = 0
print(format(hour, '2d'), ':', format(minute, '02d'), sep='')