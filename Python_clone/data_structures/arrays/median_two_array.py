def find_median_sorted_arrays(num1: list[int], num2: list[int]) -> float:
    """
    Find the median of two arrays.

    Args:
        nums1: The first array.
        nums2: The second array.

    Returns:
    The median of the two arrays.

    Examples:
        >>> find_median_sorted_arrays([1, 3], [2])
        2.0

        >>> find_median_sorted_arrays([1, 2], [3, 4])
        2.5

        >>> find_median_sorted_arrays([0, 0], [0, 0])
        0.0

        >>> find_median_sorted_arrays([], [])
        Traceback (most recent call last):
            ...
        ValueError: 둘다 비었음

        >>> find_median_sorted_arrays([], [1])
        1.0

        >>> find_median_sorted_arrays([-1000], [1000])
        0.0

        >>> find_median_sorted_arrays([-1.1, -2.2], [-3.3, -4.4])
        -2.75
    """
    if not num1 and not num2:
        raise ValueError("둘다 비었음")

    merged = sorted(num1 + num2)
    total_len = len(merged)
    if total_len % 2 == 1:  # 홀수면
        return float(merged[total_len//2])  # 몫만 취한다.
    
    middle1 = merged[total_len//2 - 1]
    middle2 = merged[total_len//2]
    
    return (float(middle1) + float(middle2)) / 2.0

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)