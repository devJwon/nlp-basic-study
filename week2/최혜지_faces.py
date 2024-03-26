def main() :
    emoji = convert_emoji(input("You can use ':)' or ':(' to express your feelings in"))
    print(emoji)

def convert_emoji(d) :
    if d == ":)" :
        return "🙂"

    elif d == ":(" :
        return "🙁"
    else :
        print("You can use only ':)' or ':('")

main()