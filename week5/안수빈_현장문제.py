"""When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase."""

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    no_vowels = ""
    for char in text:
        if char not in vowels:
            no_vowels += char
    return no_vowels

twitter = input("Please enter the text: ")

print(remove_vowels(twitter))