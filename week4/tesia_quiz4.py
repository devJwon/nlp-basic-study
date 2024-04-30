#event, 1 person gets coffee, 3 get chicken (if you get one prize, yo cannot get another)
#20 people comments, their usernames 1-20
#sort the info regardles of what the content of the comment is, duplicates are forbidden 
#use shuffle and sample from random

from random import *
customers = range(1,21)
customers1 = list(customers) #why does it not accept set?
shuffle(customers1)
recipients = sample(customers1, 4)

print("coffee: {0}".format(recipients[0]))
print("chicken: {0}".format(recipients[1:]))
