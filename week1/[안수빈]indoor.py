'''
추가 문제 1번

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

indoor.py 이라는 파일에서 사용자에게 입력을 요청하는 프로그램을 파이썬으로 구현한 다음 입력받은 내용을 소문자로 출력하세요. 문장 부호와 공백 부호는 그대로 출력해야 합니다. 사용자에게 명시적으로 프롬프트를 제공하는 것은 환영하지만, 이를 위해 자신의 문자열을 input 함수의 인자로 전달하는 것은 필수가 아닙니다.

=> 사용자의 입력창에 나타나는 '텍스트를 입력해 주세요.' 같은 프롬프트가 꼭 없어도 된다는 의미.
'''

text_input = input()

print(text_input.lower())