from random import sample

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
chicken = sample(lst, 1)[0]
print("치킨 구폰 당첨자는 " + str(chicken) + "입니다")

lst_copy = lst.copy()  
lst_copy.remove(chicken)  

coffee = sample(lst_copy,3)
print("커피 구폰 당첨자는 " + str(coffee) + "입니다")
