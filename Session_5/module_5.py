from collections import Counter
import os
import re
from pathlib import Path
from random import choice
from random import seed
from typing import List, Union

import requests
from requests.exceptions import ConnectionError

# from gensim.utils import simple_preprocess


S5_PATH = Path(os.path.realpath(__file__)).parent

PATH_TO_NAMES = S5_PATH / "names.txt"
PATH_TO_SURNAMES = S5_PATH / "last_names.txt"
PATH_TO_OUTPUT = S5_PATH / "sorted_names_and_surnames.txt"
PATH_TO_TEXT = S5_PATH / "random_text.txt"
PATH_TO_STOP_WORDS = S5_PATH / "stop_words.txt"


def task_1():
    seed(1)
    with open(PATH_TO_NAMES, 'r') as names_file:
        names = names_file.readlines()
        new_names = [i.replace('\n', '').lower() for i in names]
    with open(PATH_TO_SURNAMES, 'r') as last_names_file:
        surnames = [i for i in last_names_file.readlines()]
    full_names = [name + ' ' + choice(surnames) for name in sorted(new_names)]
    with open(PATH_TO_OUTPUT, 'w') as names_file:
        names_file.writelines(full_names)


def task_2(top_k: int):
    with open(PATH_TO_STOP_WORDS, 'r') as f:
        stop_words = set(f.read().splitlines())
    with open(PATH_TO_TEXT, 'r') as f:
        text = f.read().lower()
    words = re.findall(r"[a-z]+", text)
    filtered_words = [word for word in words if word not in stop_words]
    counter = Counter(filtered_words)
    return counter.most_common(top_k)


def task_3(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except ConnectionError:
        raise


def task_4(data: List[Union[int, str, float]]):
    res = 0
    try:
        return sum(data)
    except TypeError:
        for i in data:
            try:
                res += float(i)
            except (TypeError, ValueError):
                raise TypeError
        return res


def task_5():
    try:
        a, b = input().split()
        a = float(a)
        b = float(b)

        if b == 0:
            print("Can't divide by zero")
        else:
            print(a / b)

    except ValueError:
        print("Entered value is wrong")
