from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 12


def task1():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")
    presents = []
    for present_data in data[:-1]:
        present = set()
        present_data = present_data[1:]
        for y, line in enumerate(present_data):
            for x, c in enumerate(line):
                if c == "#":
                    present.add((x, y))
        presents.append(present)
    regions = data[-1]
    ans = 0
    for region in regions:
        size, needed = region.split(": ")
        width, length = [int(e) for e in size.split("x")]
        needed = [int(e) for e in needed.split(" ")]
        size_needed = sum([len(presents[i]) * n for i, n in enumerate(needed)])
        if size_needed > width * length:
            continue
        ans += 1
    print(ans)
    return ans


task1()
