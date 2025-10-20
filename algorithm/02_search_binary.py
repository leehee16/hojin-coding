# def is_existing_target_number_binary(target, array):
#     cur_min_idx = 0
#     cur_max_idx = len(array)-1
#     middle_idx = (cur_min_idx+cur_max_idx)//2
#     middle = array[middle_idx]
#     if cur_max_idx == 0:
#         if middle == target:
#             return True
#         else: return False
#     if middle == target:
#         return True
#     if middle > target:
#         is_existing_target_number_binary(target, array[middle+1:cur_max_idx-1])
#     if middle < target:
#         is_existing_target_number_binary(target, array[cur_min_idx:middle-1])

def is_existing_target_number_binary(target, array):
    if len(array) == 0:
        return False

    middle_idx = len(array) // 2
    middle = array[middle_idx]

    if middle == target:
        return True
    elif middle < target:
        return is_existing_target_number_binary(target, array[middle_idx+1:])
    else:
        return is_existing_target_number_binary(target, array[:middle_idx])

def binary_search(target, array):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = array[mid]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)