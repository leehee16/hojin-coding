array = [5, 3, 2, 1, 6, 8, 7, 4]

def merge(array1, array2):
    result = []
    a1_idx = 0
    a2_idx = 0
    while a1_idx < len(array1) and a2_idx < len(array2):
        if array1[a1_idx] > array2[a2_idx]:
            result.append(array2[a2_idx])
            a2_idx += 1
        else :
            result.append(array1[a1_idx])
            a1_idx += 1
    while a1_idx < len(array1):
        result.append(array1[a1_idx])
        a1_idx += 1

    while a2_idx < len(array2):
        result.append(array2[a2_idx])
        a2_idx += 1
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left,right)

print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))