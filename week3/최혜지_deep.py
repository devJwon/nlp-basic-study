def main() :
    answer = input('Please enter the answer to the Great Question of Life, the Universe and Everything.')
    user_answer = answer.lower()
    
    if user_answer in ["42", "forty-two", "forty two"]:
        print("Yes")
    else :
        print("No")

main()