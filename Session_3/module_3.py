import time
from typing import List

Matrix = List[List[int]]


def task_1(exp: int):
    def power_factory(base):
        return base ** exp

    return power_factory


def task_2(*args, **kwargs):
    for arg in args:
        print(arg)
    for value in kwargs.values():
        print(value)


def helper(func):
    def wrapper(*args, **kwargs):
        print("Hi, friend! What's your name?")
        res = func(*args, **kwargs)
        print("See you soon!")
        return res

    return wrapper


@helper
def task_3(name: str):
    print(f"Hello! My name is {name}.")


def timer(func):
    def wrapper():
        time_start = time.time()
        func()
        time_end = time.time()
        run_time = time_end - time_start
        return print(f"Finished {func.__name__} in {run_time:.4f} secs")

    return wrapper


@timer
def task_4():
    return len([1 for _ in range(0, 10 ** 8)])


def task_5(matrix: Matrix) -> Matrix:
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for i in range(cols):
        result.append([])
    for col in range(cols):
        for row in range(rows):
            result[col].append(matrix[row][col])

    return result


def task_6(queue: str):
    res = 0
    for i in queue:
        if i == '(':
            res += 1
        elif i == ')':
            res -= 1
        if res < 0:
            return False

    return res == 0
