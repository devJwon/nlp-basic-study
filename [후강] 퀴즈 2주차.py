# 1번째 방법 
from random import randrange
number =randrange(4,28)
print('오프라인 스터디 모임 날짜는 매월' + str(number) + '일로 선정되었습니다.')

# 2번째 방법
from random import random
number =int(random( )*25+4) 
print('오프라인 스터디 모임 날짜는 매월' + str(number) + '일로 선정되었습니다')

# 3번째 방법
from random import randint
number =randint(4,28)
print('오프라인 스터디 모임 날짜는 매월' + str(number) + '일로 선정되었습니다')
