# 치킨 당첨자: 1
# 커피 당첨자: 2, 3, 4


from random import *


list = []
# users = list(range(1, 21))

for i in range(1, 21):
    list.append(i)
    shuffle(list)

# print("치킨 당첨자: ", sample(list, 1))
# print("커피 당첨자: ", sample(list, 3))

luckys = sample(list, 4)

print('치킨 당첨자: ', luckys[0])
print('커피 당첨자: ', luckys[1:])


# print('치킨 당첨자: {0}'.format(luckys[0]))
# print('커피 당첨자: {0}'.format(luckys[1:]))

