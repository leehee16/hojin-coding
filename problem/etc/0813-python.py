
# 0813 python
""" 01. 문자열 슬라이싱, 그런데 이제 점프
머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있습니다. 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.

제한사항
2 < numbers의 길이 < 100
0 < k < 1,000
numbers의 첫 번째와 마지막 번호는 실제로 바로 옆에 있습니다.
numbers는 1부터 시작하며 번호는 순서대로 올라갑니다.
입출력 예
numbers	k	result
[1, 2, 3, 4]	2	3
[1, 2, 3, 4, 5, 6]	5	3
[1, 2, 3]	3	2
"""
def solution(numbers, k):
    if len(numbers) % 2 == 0:
        jump = numbers[::2]
    else :
        jump = numbers[::2]+numbers[1::2]
    return jump[(k-1)%len(jump)]


"""
배열의 회전, deque로 해결했다.
"""
from collections import deque
def solution(numbers, direction):
    dq = deque(numbers)
    if direction == 'right':
        pop = dq.pop()
        dq.appendleft(pop)
    else :
        popleft = dq.popleft()
        dq.append(popleft)
    return list(dq)

"""
인덱스로 짝홀 구분,둘중 최대값 출력 
"""
def solution(num_list):
    even_sum = 0
    odd_sum = 0
    for i,v in enumerate(num_list):
        if (i+1)%2 == 0:
            even_sum += v
        else :
            odd_sum +=v
    return max(even_sum,odd_sum)


"""
초기 진입점 잡기 / inplace수정 / arr1과 arr2가 동일한 객체가 되고, while arr1 != arr2가 바로 False가 되어 조기 종료
"""
def solution(arr):
    def transfer_arr(arr):
        for i,v in enumerate(arr) :
            if v%2 == 0 and v>=50:
                arr[i] = v//2
            elif v%2 !=0 and v<50 :
                arr[i] = v*2+1
        return arr
    count = 0
    arr1 = 0
    arr2 = 1
    while arr1 != arr2 :
        if arr2 ==1 :
            arr1 = arr2
            arr2 = transfer_arr(arr)
            count += 1
        else:
            arr1 = arr2
            arr2 = transfer_arr(arr1)
            count +=1
    return count-1

"""
얕은 복사와 깊은 복사
"""
def solution(arr):
    def transfer_arr(arr):
        new_arr = arr[:]  # 얕은 복사
        for i, v in enumerate(arr):
            if v % 2 == 0 and v >= 50:
                new_arr[i] = v // 2
            elif v % 2 != 0 and v < 50:
                new_arr[i] = v * 2 + 1
        return new_arr

    count = 0
    prev = arr
    
    while True:
        nxt = transfer_arr(prev)
        if prev == nxt :
            break
        prev = nxt
        count +=1
    return count
                
"""
특정 연산의 횟수를 모두 더하는것. 이게 한번에 되네
"""

def solution(num_list):
    def count_cal(num):
        count = 0
        while True :
            if num ==1 :
                break
            if num %2 == 0:
                num=num//2
                count +=1
            else :
                num=(num-1)//2
                count +=1
        return count
    def count_cal_revision(num):
        count = 0
        while num > 1:   # break 대신 조건 직접 사용
            num //= 2    # 짝수/홀수 구분 없이 동일
            count += 1
        return count    
    return sum([count_cal_revision(a) for a in num_list])

"""
길이에 따른 연산
"""
def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else :
        a = 1
        for i in num_list:
            a *= i
        return a
# math 모듈 사용 list 모두 곱하기
import math

def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else math.prod(num_list)

"""
extend사용. 처음 마주하는값?
"""
def solution(arr, k):
    set_arr = sorted(list(set(arr)))
    ans = []
    if len(set_arr)>= k:
        ans.extend(set_arr[:k])
    else: 
        ans.extend(set_arr)
        ans.extend(-1 for _ in range(k-len(set_arr)))
    return ans

# 시도 2 : 정렬순서 교정
def solution(arr, k):
    set_arr = set_arr = list(dict.fromkeys(arr))
    ans = []
    if len(set_arr)>= k:
        ans.extend(set_arr[:k])
    else: 
        ans.extend(set_arr)
        ans.extend(-1 for _ in range(k-len(set_arr)))
    return ans

# 시도 3 : 그냥 if문으로 채우기
def solution(arr, k):
    set_list = []
    for i in arr : 
        if not i in set_list :
            set_list.append(i)
    
    if len(set_list) >= k:
        return set_list[:k]
    else :
        set_list.extend([-1 for _ in range(k-len(set_list))])
        return set_list
    

"""
정수 배열 arr이 매개변수로 주어집니다. arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다. arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.

제한사항
1 ≤ arr의 길이 ≤ 1,000
1 ≤ arr의 원소 ≤ 1,000
입출력 예
arr	result
[1, 2, 3, 4, 5, 6]	[1, 2, 3, 4, 5, 6, 0, 0]
[58, 172, 746, 89]	[58, 172, 746, 89]
"""
import math
def solution(arr) :
    def binary_ceiling(decimal):
        ceiling = 2 ** math.ceil(math.log2(decimal))
        return bin(ceiling)[2:]
    if binary_ceiling(len(arr)) >= len(arr):
        return 