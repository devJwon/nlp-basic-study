'''
문자열 처리 퀴즈
프로그래밍 세계에서 사용자 입력을 다루는 일은 흔한 작업입니다. 종종 이 입력은 다양한 목적을 위해 검증되거나 파싱되거나 조작되어야 합니다. 이름이나 제목을 처리하고 살균하는 것은 이러한 작업의 고전적인 예입니다. 특히 이들을 특정 형식이나 기준에 맞춰서 유지하는 것이 중요합니다.

컨퍼런스 등록 양식을 만드는 시나리오를 상상해 보세요. 양식에는 참석자들이 전체 이름을 입력하는 필드가 포함되어 있습니다. 그러나 참석자 배지와 기록에서 통일된 형식을 유지하기 위해 이름 입력에 대한 특정 규칙을 구현하기로 결정했습니다. 구체적으로, 이름의 각 부분이 대문자로 시작하고 그 뒤에 소문자가 이어지도록 하려고 합니다. 참석자가 원래 어떻게 타이핑하든 상관없이 말이죠. 추가로, 간단히 하기 위해 각 이름이 이름과 성 두 부분만으로 구성되어 있으며, 단일 공백으로 구분된다고 가정합니다.

예를 들어, 참석자가 "john doe", "John Doe", "JOHN DOE" 또는 다른 변형을 타이핑하는 경우, 시스템은 이를 "John Doe"로 포맷해야 합니다.

이 시나리오를 바탕으로 format_name.py라는 이름의 파이썬 프로그램을 만드는 것이 여러분의 과제입니다. 이 프로그램은 사용자에게 어떤 대소문자 형식이든 전체 이름을 입력하도록 요청해야 합니다. 입력을 받은 후에는 위에서 언급한 규칙에 따라 이름을 포맷된 형식으로 출력해야 합니다: 이름의 각 부분은 대문자로 시작해야 하며 그 뒤에 소문자가 이어져야 하고, 두 부분은 단일 공백으로 구분되어야 합니다.

다음은 고려해야 할 몇 가지 테스트 케이스입니다:

입력: "jane DOE"

출력: "Jane Doe"

입력: "aLEXander Hamilton"

출력: "Alexander Hamilton"

입력: "aNNA kARENINA"

출력: "Anna Karenina"

이름이 정확히 두 부분을 포함하지 않는 경우(예를 들어, 성이 빠지거나 중간 이름이 포함된 경우), 프로그램은 "이름과 성만 입력해주세요."라는 오류 메시지를 출력해야 합니다.

이 도전은 split(), capitalize()와 같은 파이썬의 문자열 메소드와 조건문을 사용하여 다양한 입력 사례를 처리하는 지식이 필요합니다. 문자열 조작과 사용자 입력 검증을 연습하기에 훌륭한 연습문제입니다.
'''
# 풀이 1
name = input().split()

new_name = []
for word in name:
    new_name.append(word[0].upper()+word[1:].lower())

print(' '.join(new_name))

# 풀이 2
name = input().split()

new_name = []
for word in name:
    new_name.append(word.capitalize())

print(' '.join(new_name))

# 풀이 3
print(input().title())


