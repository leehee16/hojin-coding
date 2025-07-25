def product_sum(arr: list[int | list], depth: int) -> int :
    total_sum = 0
    for ele in arr:
        # list를 인지하면 1, depth에 따른 판단을 어떻게 하지.
        total_sum += product_sum(ele, depth + 1) if isinstance(ele, list) else ele
    return total_sum * depth


def product_sum2(arr:list[int|list], depth:int) -> int :
    total_sum = 0 
    for ele in arr :
        if isinstance(ele,int):
            total_sum += ele
        else : total_sum += product_sum2(ele, depth+1)
        #total_sum += ele if isinstance(ele,int) else product_sum2(ele, depth+1)
    return total_sum*depth
