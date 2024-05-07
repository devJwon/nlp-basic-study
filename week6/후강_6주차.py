def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height = 175
gender = "남자"
weight= round(std_weight(height / 100, gender),2)
print("키" + str(height) + "cm" + gender + "의 표준 체준은" + str(weight) + "kg입니다")