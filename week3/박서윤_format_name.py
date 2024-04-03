# title 사용
while True:
  temp_name = input("What is your name sir/ma'am? ")
  
  if len(temp_name.split()) == 2:
    real_name = temp_name.title()
    print(f"Welcome Aboard, {real_name}!")
    break
    
  else:
    print("Error: only first and last name please")


# caplitalize 사용
while True:
    temp_name = input("What is your name sir/ma'am? ")

    if len(temp_name.split()) == 2:
        real_name = temp_name.split()
        first = real_name[0].caplitalize()
        last = real_name[1].caplitalize()
        new_name = first+" "+last

        print(f"Welcome Aboard, {new_name}!")
        break
    else:
        print("Error: only first and last name please")
