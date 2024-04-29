""" 
당신은 Cocoa 서비스를 이용하는 택시 기사님입니다. 
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건 2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[〇] 1번째 손님 (소요시간: 15분)
[  ] 2번째 손님 (소요시간: 50분)
[〇] 3번째 손님 (소요시간: 5분)
…
[  ] 50번째 손님 (소요시간: 16분)

총 탑승 승객: 2분
"""

import random

total_passengers = 50
matched_passengers = 0

for passenger in range(1, total_passengers + 1):
    ride_time = random.randint(5, 50)
    if 5 <= ride_time <= 15:
        print("[〇] {0}번째 손님 (소요시간: {1}분)".format(passenger, ride_time))
        matched_passengers += 1
    else:
        print("[  ] {0}번째 손님 (소요시간: {1}분)".format(passenger, ride_time))

print("총 탑승 승객: {0}분".format(matched_passengers))

# GPT 도움 받았음
