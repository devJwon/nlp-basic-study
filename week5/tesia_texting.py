# shorten words
# input string of text
#output text in shortened ver.

ommitt = ['a', 'e', 'i', 'o', 'u']

word = input("please input word:")
word1 = word.lower()

for char in word1:
    if char in ommitt:
        continue
    else:
       print(char, end='')
