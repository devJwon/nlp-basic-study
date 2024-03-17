'''
추가 문제 2번

Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).
'''

text_input = input("문장을 입력하세요: ")

modified_input = text_input.replace(" ", "...")

print(modified_input)