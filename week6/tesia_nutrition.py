def fruits():
    fruit = {
        "bananas": 65,
        "apples": 130,
        "avocados": 50,
        "grapes": 90,
        "grapefruits": 60}
    return fruit

def main():
    fruit_dict = fruits()
    BuyFruit = input("please input the fruit you want to buy:")
    buy = BuyFruit.lower()

    if buy in fruit_dict:
        print("this fruit has {0} calories/g".format(fruit_dict[buy]))
    else:
        print("try again")

main()