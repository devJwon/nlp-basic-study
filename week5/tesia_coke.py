"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, 
and ignore any integer that isn’t an accepted denomination.
"""
def coins():
    coin_value = [5, 25, 10]
    sum = 0

    while sum < 50:
        c = int(input("please insert a coin of 5,25 or 10 cents:")) 
        if c not in coin_value:
            continue
        else:
            sum += c
            print(50 - sum)
    return sum

coins()
    
