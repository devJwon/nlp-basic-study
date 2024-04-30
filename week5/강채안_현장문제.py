mouem = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

char = input('단어를 입력하세요: ')
letter = ''


for i in char:
    if i not in mouem:
        letter += i
print(letter)


for i in range(len(char)):
    if char[i] not in mouem:
        letter += char[i]
print(letter)


