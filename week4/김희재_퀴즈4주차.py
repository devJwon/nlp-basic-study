from random import*

users = range(1, 21) #1부터 20까지 숫자를 생성
print(users)
users = list(users)
#print(type(users))

print(users)
shuffle(users)
print(users)

winner = sample(users, 4)  #4명 중 1명 치킨, 3명 커피
print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))
print("--축하합니다!")
