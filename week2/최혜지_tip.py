def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars_float = float(d.replace('$', ''))
    return dollars_float


def percent_to_float(p):
    percent_float = float(p.replace('%', '')) * 0.01
    return percent_float


main()
