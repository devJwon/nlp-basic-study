from random import *

total = 0

for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print('[0]', i, '번째 손님 소요시간:', time)
        total += 1
    else:
        print('[ ]', i, '번째 손님 소요시간:', time)

print('총 탑승 승객: ', total)

