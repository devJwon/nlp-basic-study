def main() :
    user_name = convert_snake(input("Please enter a name in camel case : "))
    print(user_name)

def convert_snake(camel_name) :
    snake_name = ""
    for char in camel_name :
        if char.isupper() :
            snake_name += "_" + char.lower()
        else :
            snake_name += char
    
    return snake_name.lstrip("_")

main()