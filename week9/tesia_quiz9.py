'''
condition 1: if the num is smaller than 1 or is not a number --> value error "you entered an invalid value"
condition 2: the number of chickens for sale is 10. if the value decreases to 0 --> sold out error "the limit has been reached. we cannot receive your order"

'''
class SoldOutError(Exception):
    pass


chicken = 10
waiting = 1

while True:
    try: 
        print("remaining chickens: {0}".format(chicken))
        order = int(input("how many chickens do you wish to buy?"))
        if order <= 0:
            raise ValueError

        elif order > chicken:
            print("insufficient ingredients")
        else:
            print("waiting number {0}, {1} chicken order completed".format(waiting, order))
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError
    

    except ValueError:
        print("the limit has been reached. we cannot receive your order")
            
    except SoldOutError:
        print("you entered an invalid value")
        break




