'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

예) http://naver.com
규칙1: http:// 부분은 제외 => naver.com
규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3: 남은 글자 중 처음 세 자리 + 글자 개수 + 글자 내 'e' 개수 + "!"로 구성
                (nav)               (5)              (1)        (!)
예) 생성된 비밀번호: nav51!
'''

website_input = input("사이트의 주소를 입력해 주세요: ")

website = website_input.replace("http://", "")
website = website[:website.index(".")]
password = website[:3] + str(len(website)) + str(website.count('e')) + "!"

print("{0}의 비밀번호는 {1}입니다.".format(website_input, password))