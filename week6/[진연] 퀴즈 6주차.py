def sta_weight(height, gender):
    if gender == "남":
       print("키 {} 남자의 표준 체중은 {:.2f}kg 입니다.".format(height, height*height*22))
    else:
       print("키 {} 여자의 표준 체중은 {:.2f}kg 입니다.".format(height, height*height*21))

sta_weight(1.65, "여")
