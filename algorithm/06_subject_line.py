#2019년 상반기 line 인턴 채용 코딩테스트 : 나잡아봐라.
from collections import deque

c = 11
b = 2


def first_catch_me(cony_loc, brown_loc):
    time = 0
    cony_start = cony_loc
    while cony_loc <= 200000 and cony_loc > brown_loc:
        time += 1
        cony_loc = cony_start + (time*(time+1))//2
        brown_loc = max((brown_loc-1,brown_loc+1,brown_loc*2))
    
    return time

def catch_me(cony_loc, brown_loc):
    time = 0
    brown_que = deque()
    brown_dict = {time:brown_que}

    while cony_loc <= 200000 and cony_loc > brown_loc:
        time += 1
        cony_loc += time
        
    
    return time



print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))