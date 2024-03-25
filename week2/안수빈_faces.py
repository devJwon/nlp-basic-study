'''
Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.
'''

def convert(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

def main():
    user_input = input("텍스트를 입력하세요: ")
    converted_text = convert(user_input)
    print("변환 결과:", converted_text)

if __name__ == "__main__": # 챗gpt의 도움으로 코드 작성. 해당 부분에 대해서는 설명을 보았으나 이해하지 못함...
    main()
