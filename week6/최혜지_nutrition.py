fruit_calorie = {"Apple": 52, "Banana": 105, "Grape": 62, "Orange": 62, "Peach": 59}

user_input = input("Enter a fruit: ").capitalize()

if user_input in fruit_calorie:
    calories_per_portion = fruit_calorie[user_input]
    print(f"The number of calories in one portion of {user_input} is {calories_per_portion}.")
else:
    print("That's not a valid fruit. Try again.")