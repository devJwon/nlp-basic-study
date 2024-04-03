''' 
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하세요

예: http://naver.com
http 부분 제외 naver.com
처음 만나는 점(.) 이후 부분 제외 --> naver
남은 글자  중 처음 세자리 +  글자 갯수 + 글자 내 'e' + "!" 로 구성
'''

address =  "http://naver.com"
address = address[7:]
#print(address)

address = address[:5]
#print(address)

address = address[:3] + str(len(address)) + str(address.count("e")) + "!"
print("My password:" + address)
