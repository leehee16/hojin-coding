import functools
import time


def log_duration(fn):
    """Measure the wall-clock time for the outermost invocation."""
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        depth = getattr(wrapper, "_call_depth", 0)
        setattr(wrapper, "_call_depth", depth + 1)
        start = time.perf_counter()
        try:
            result = fn(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            setattr(wrapper, "_call_depth", depth)
        if depth == 0:
            print(f"{fn.__name__} took {elapsed:.6f}s")
        return result

    return wrapper


@log_duration
def first_fibo(number: int) -> int:
    if number <= 0:
        raise ValueError("양수만 허용됩니다.")
    if number <= 2:
        return 1

    num_list = [1, 1]
    while len(num_list) < number:
        num_list.append(num_list[-1] + num_list[-2])
    return num_list[-1]


@log_duration
def my_recursive_fibo(number: int) -> int:
    if number is None or number <= 0:
        raise ValueError("양수만 허용됩니다.")
    if number <= 2:
        return 1
    return my_recursive_fibo(number - 1) + my_recursive_fibo(number - 2)


@log_duration
def my_dp_fibo(number: int, memory: dict[int, int] | None = None) -> int:
    if number <= 0:
        raise ValueError("양수만 허용됩니다.")
    if memory is None:
        memory = {1: 1, 2: 1}

    if number in memory:
        return memory[number]

    memory[number] = my_dp_fibo(number - 1, memory) + my_dp_fibo(number - 2, memory)
    return memory[number]


if __name__ == "__main__":
    print(f"그냥 반복문 : {first_fibo(number=30)}")
    print(f"재귀문 : {my_recursive_fibo(number=30)}")
    print(f"동적 계획법 : {my_dp_fibo(30)}")
