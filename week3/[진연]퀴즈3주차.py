URL = "http://naver.com"
my_str = URL.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print(f"{URL}의 비밀번호는 {password}입니다.")
