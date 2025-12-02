from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 2


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data = data[0].split(",")
    ids = 0
    for r in data:
        first, last = [int(e) for e in r.split("-")]
        for n in range(first, last + 1):
            if is_invalid(str(n)):
                ids += n
    ans = ids
    print(ans)


def is_invalid(id: str) -> bool:
    if len(id) % 2 == 1:
        return False
    middle = len(id) // 2
    return id[:middle] * 2 == id


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data = data[0].split(",")
    ids = 0
    for r in data:
        first, last = [int(e) for e in r.split("-")]
        for n in range(first, last + 1):
            if is_invalid2(str(n)):
                print(f"found {n} in {first}-{last}")
                ids += n
    ans = ids
    print(ans)


def is_invalid2(id: str) -> bool:
    for i in range(len(id) // 2):
        substr = id[: i + 1]
        repeats = len(id) // len(substr)
        if substr * repeats == id:
            return True
    return False


task1()
task2()
