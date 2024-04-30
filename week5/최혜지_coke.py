def main():
    amount_due = 50
    amount_inserted = 0

    while amount_inserted < amount_due:
        coin = int(input("Insert a coin (25, 10, or 5 cents): "))
        if coin == 25 or coin == 10 or coin == 5:
            amount_inserted += coin
            print("Amount due:", amount_due - amount_inserted, "cents remaining")
        else:
            print("Invalid denomination. Only 25, 10, or 5 cents are accepted.")

    change = amount_inserted - amount_due
    print("Change owed:", change, "cents")


main()