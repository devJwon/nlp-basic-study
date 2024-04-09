# main() 아직 익숙하지 않아 냅다 만들었습니다 ... !

user_time = input('식사 언제 하세욤: ')
user_hour = float(user_time.split(':')[0])

if user_hour == 7:
    print('굿모닝 아침 먹고 가세요 ~')
elif user_hour == 12:
    print('점심 타임 !')
elif user_hour == 18:
    print('저녁드세욤!')
else:
    print('밥 먹을 시간 아닙니다ㅠ')
