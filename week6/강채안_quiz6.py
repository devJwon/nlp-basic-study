def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = float(input('키 입력하세요: '))
gender = input('성별 입력: ')

weight = round(std_weight(height / 100, gender), 2)
print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height, gender, weight))

    
