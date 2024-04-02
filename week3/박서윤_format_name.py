temp_name = input("What is your name sir/ma'am? ")
if len(temp_name) ==2:
  real_name = temp_name.title()
  print(f"Welcome, {real_name}!")
else:
  print("only first and last name please")
