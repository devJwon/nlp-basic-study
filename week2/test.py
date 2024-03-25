# from jaewon_faces import convert
import jaewon_faces

def main():
    user_input = input("Enter some text: ")
    converted_text = jaewon_faces.convert(user_input)
    print(converted_text)

if __name__ == "__main__":
    main()
