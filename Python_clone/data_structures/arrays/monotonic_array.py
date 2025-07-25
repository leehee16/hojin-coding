'''
Monotonic Array(단조 배열)는 배열의 모든 요소가 단조적으로 증가하거나 감소하는 배열입니다.
🔍 두 가지 유형
Monotonic Increasing (단조 증가)
각 요소가 이전 요소보다 크거나 같음
예: [1, 2, 2, 3], [-3, -2, -1], [0, 0, 0]
Monotonic Decreasing (단조 감소)
각 요소가 이전 요소보다 작거나 같음
예: [6, 5, 4, 4], [-5, -6, -7]
'''

def is_monotonic(nums: list[int]) -> bool:
    """
    리스트가 Monotonic한지 체크
    >>> is_monotonic([1, 2, 2, 3])
    True
    >>> is_monotonic([6, 5, 4, 4])
    True
    >>> is_monotonic([1, 3, 2])
    False
    >>> is_monotonic([1,2,3,4,5,6,5])
    False
    >>> is_monotonic([-3,-2,-1])
    True
    >>> is_monotonic([-5,-6,-7])
    True
    >>> is_monotonic([0,0,0])
    True
    >>> is_monotonic([-100,0,100])
    True
    """
    return all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or all(
        nums[i] >= nums[i+1] for i in range(len(nums)-1)
    )

# test
if __name__ == "__main__":
    print(is_monotonic([1,2,3,4,5,7]))
    print(is_monotonic([1,3,5,7]))
    print(is_monotonic([7,6,5,3,1]))
    
    import doctest
    doctest.testmod(verbose=True)