def main():
    amount_due = 50
    accepted_coins = [25, 10, 5]
    
    print("Please insert coins.")
    
    while amount_due > 0:
        coin = int(input("Insert a coin: "))
        
        if coin in accepted_coins:
            amount_due -= coin
            if amount_due > 0:
                print(f"Amount due: {amount_due}")
        else:
            print(f"Invalid coin. Amount due: {amount_due}")
    
    change = abs(amount_due)
    print(f"Change owed: {change}")

if __name__ == "__main__":
    main()