while True:
  temp_name = input("What is your name sir/ma'am? ")
  if len(temp_name.split()) ==2:
    real_name = temp_name.title()
    print(f"Welcome, {real_name}!")
    break
  else:
    print("only first and last name please")
