"""
정수로 이루어진 배열과 하나의 정수 req_sum이 주어졌을 때, 
배열 원소들 중 두 수의 합이 req_sum이 되는 쌍의 개수를 구하시오.
"""

from itertools import combinations

def pairs_with_sum(arr: list, req_sum: int) -> int :
    """
    Return the no. of pairs with sum "sum"
    >>> pairs_with_sum([1, 5, 7, 1], 6)
    2
    >>> pairs_with_sum([1, 1, 1, 1, 1, 1, 1, 1], 2)
    28
    >>> pairs_with_sum([1, 7, 6, 2, 5, 4, 3, 1, 9, 8], 7)
    4
    """
    return len([1 for a,b in combinations(arr,2) if a+b == req_sum])


#test
if __name__=="__main__":
    from doctest import testmod
    testmod(verbose=True)    