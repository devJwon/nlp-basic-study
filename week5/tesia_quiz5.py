'''
#cocoa taxi service , 50 customers
#distance time for each customer is between 5-50 min 
#you only should pick up the customers at a distance of 5-15 minutes
'''
from random import *
index = 0

for customer in range(1,51):
    distance_limit = randrange(1, 51)

    if 5 <= distance_limit <= 15:
        #pick up
        print("[0] customer {0}, used time: {1}".format(customer, distance_limit))
        index += 1

    else:
        print("[ ] customer {0}, used time: {1}".format(customer, distance_limit))


print("customers so far: {0}".format(index))