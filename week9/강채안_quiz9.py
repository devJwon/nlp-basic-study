class SoldOutError(Exception):
    pass

chichen = 10
waiting = 1

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chichen))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chichen:
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." \
                .format(waiting, order))
            waiting += 1
            chichen -= order
            
        if chichen == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 모두 소진되었습니다.")
        break