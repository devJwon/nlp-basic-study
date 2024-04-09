def main():  # 사용자에게 시간을 입력 받
    time = input("지금 몇 시...? 맘마 안 드시나...") #사용자에게 시간 입력하도록 요청
    hour = convert(time) # 시간 형식 변환

    if 7 <= hour < 8:
        print("아침 맘마!")
    elif 12 <= hour < 13:
        print("점심 맘마!")
    elif 18 <= hour < 19:
        print("저녁 맘마")

def convert(time): # 입력된 시간을 부동 소수점 형식으로 변환
    hours, minutes = map(int, time.splite(':')) # 시간과 분 분리
    return hours + minutes / 60

if __name__ == "__main__": # 파이썬 실행될때 main 함수 호출
    main()