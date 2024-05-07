"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, 
as by omitting vowels, much like Twitter was originally called twttr. 
In a file called twttr.py, 
implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
whether inputted in uppercase or lowercase.
"""
def main() :
    user_input = del_aeiou(str(input("Enter any word : ")))
    print(user_input)

element = 'aeiou'

def del_aeiou(word) :
    new_word = []
    for char in word :
        if char.lower() not in element :
            new_word.append(char)
    return ''.join(new_word)

main()

        