"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

def get_change(payment, price):
    change = payment - price
    return change

def main():
    coke_price = 50
    payment = 0

    while payment < coke_price:
        try:
            coin = int(input("동전을 넣어주세요 (25, 10, 5 센트만 가능합니다): "))
            if coin == 25 or coin == 10 or coin == 5:
                payment += coin
            else:
                print("25, 10, 5 센트만 가능합니다.")
        except ValueError:
            print("정수만 입력해주세요.")

    change = get_change(payment, coke_price)
    print("거스름돈은 {0} 센트입니다.".format(change))

if __name__ == "__main__":
    main()
