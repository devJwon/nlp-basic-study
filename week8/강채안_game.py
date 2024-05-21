import random

while True:
    try:
        level = int(input('정수만 입력!!: '))
        if level > 0:
            break
        else:
            print('정수만 입력하랬지')
    except ValueError:
        print('정수만 다시 입력!!')


# level = 3
num = random.randint(1, level)
# print(num)

# if num < user_num:
#     print("넘 작 !")
# elif num > user_num:
#     print("넘 큼 !")
# else:
#     print("맞!")


while True:
    if num < level:
        print("넘 큼 !")
        level = int(input('다시 입력: '))
    elif num > level:
        print("넘 작 !")
        level = int(input('다시 입력: '))
    else:
        print("맞!")
        print(num)
        break
