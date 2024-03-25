# plain code
expression = input('emoji converter: ')
if ':)' or ':(' in expression:
    expression = expression.replace(':)','🙂')
    expression = expression.replace(':(','🙁')
    print(expression)

else:
    print(expression)

# main function
def main():
    expression = input('emoji converter: ')
    print(convert(expression))

def convert(string):
    if ':)' or ':(' in string:
        string_converted = string.replace(':)', '🙂').replace( ':(', '🙁')
        return string_converted

    else:
        string
        return string
