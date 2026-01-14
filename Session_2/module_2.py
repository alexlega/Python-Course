# from collections import defaultdict as dd
# from itertools import product
from typing import Any, Dict, List, Tuple


def task_1(data_1: Dict[str, int], data_2: Dict[str, int]):
    result = {}

    for key in data_1:
        if key in data_2:
            result[key] = data_1[key] + data_2[key]
        else:
            result[key] = data_1[key]

    for key in data_2:
        if key not in result:
            result[key] = data_2[key]

    return result


def task_2():
    result = {}
    for i in range(1, 16):
        result[i] = i ** 2
    return result


def task_3(data: Dict[Any, List[str]]):
    result = ['']
    for letters in data.values():
        new_result = []
        for prefix in result:
            for ch in letters:
                new_result.append(prefix + ch)
        result = new_result

    return result


def task_4(data: Dict[str, int]):
    keys = []
    values = []
    res = []
    for key, value in data.items():
        keys.append(key)
        values.append(value)
    while (len(res) != 3) and (len(values) != 0):
        res.append(keys[values.index(max(values))])
        keys.pop(values.index(max(values)))
        values.pop(values.index(max(values)))
    return res


def task_5(data: List[Tuple[Any, Any]]) -> Dict[str, List[int]]:
    result = {}

    for key, value in data:
        if key not in result:
            result[key] = []

    for key, value in data:
        result[key].append(value)

    return result


def task_6(data: List[Any]):
    return list(zip(data))


def task_7(words: [List[str]]) -> str:
    prefix = ''

    for char_num in range(len(words[0])):
        for word in words[1:]:
            try:
                if words[0][char_num] != word[char_num]:
                    return prefix
            except IndexError:
                return prefix
        prefix += words[0][char_num]

    return prefix


def task_8(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    n = len(needle)
    h = len(haystack)
    for i in range(h - n + 1):
        if haystack[i] == needle[0]:
            if haystack[i:i + n] == needle:
                return i
    return -1
