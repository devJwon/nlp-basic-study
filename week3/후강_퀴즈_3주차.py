url = input("인터넷 주소를 입력해주세요:")

# 'www.' 가 포함되어 있는지 확인하고 제거합니다.

if "www" not in url:
    date1 = url
else:
    date1 = url.replace("www.", "")

# 첫 번째 '.' 의 위치를 찾습니다.
date2 = date1.index(".")

# ".com" 앞의 부분만 추출합니다.
date1 = date1[:date2]

#"https://"를 제거합니다
date1 = date1[len("https://")-1:]

password=date1[:3] + str(len(date1)) + str(date1.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))