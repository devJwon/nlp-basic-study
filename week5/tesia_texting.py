# shorten words
# input string of text
#output text in shortened ver.

ommit = ['a', 'e', 'i', 'o', 'u']

word = input("please input word:")
word1 = word.lower()

for char in word1:
    if char in ommit:
        continue
    else:
       print(char, end='')
