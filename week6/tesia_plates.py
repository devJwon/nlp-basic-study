
#In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car:

#at least two letters.”
#maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
#Numbers cannot be used in the middle of a plate; they must come at the end
#The first number used cannot be a ‘0’.
#No periods, spaces, or punctuation marks are allowed.
'''
output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase. 
Structure your program per the below, wherein is_valid returns True if s meets all requirements
and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement)."""
'''

plates = input("input plate name:")
plate = plates.upper()

def plate_length(plate):
    return 2 <= len(plate) <= 6

def plate_structure(plate):
    return plate.isalnum()

def order(plate):
    if plate[-1].isdigit() and not plate[0].isdigit() and plate[0] != '0':
       return True
    else:
        return False
    
def evaluation(plate):
    valid = [plate_length(plate), plate_structure(plate), order(plate)]
    return all(valid)

if evaluation(plate):
    print("Valid")
else:
    print("Not Valid")
 