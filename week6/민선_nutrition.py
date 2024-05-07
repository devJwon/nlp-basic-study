"""
The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”
In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
"""

def main():
    fruit_calories = {
        "사과": 52,
        "바나나": 89,
        "오렌지": 62,
        "딸기": 32,
        "포도": 67,
    }

    fruit = input("과일을 입력하세요들레히: ")

    if fruit in fruit_calories:
        print(f"{fruit} 한 개의 칼로리는 {fruit_calories[fruit]} 입니다.")
        # f-string: 문자열 안에 변수값 삽입, 문자열 앞에 f 붙이고 중괄호{} 안에 변수나 표현식 넣기
    else:
        print("허걱쓰 죄송합니다. 해당하는 과일의 칼로리 정보를 찾을 수 없습니다.")

if __name__ == "__main__":
    main()


