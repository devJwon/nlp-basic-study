'''
추가 문제 2번

Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, 
or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... 
(i.e., three periods).
''' 

sentence = input("Please input a sentence of your liking:" )
newSentence = sentence.replace(' ', '...')

print("here is your sentence in a slower version:", newSentence)
