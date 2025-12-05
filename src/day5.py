from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 5


def task1():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")
    ranges_data, ingredients = data
    ingredients = [int(e) for e in ingredients]
    ranges = []
    for r in ranges_data:
        a, b = [int(e) for e in r.split("-")]
        ranges.append((a, b))
    fresh = set()
    for ingredient in ingredients:
        for a, b in ranges:
            if a <= ingredient <= b:
                fresh.add(ingredient)
                break

    ans = len(fresh)
    print(ans)
    return ans


def task2():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")
    ranges_data, _ = data
    ranges = set()
    for r in ranges_data:
        a, b = [int(e) for e in r.split("-")]
        ranges.add((a, b))
    changed = True
    while changed:
        to_remove = set()
        to_add = set()
        changed = False
        for r1 in ranges:
            a1, b1 = r1
            for r2 in ranges:
                if r1 == r2:
                    continue
                a2, b2 = r2
                if a2 <= a1 <= b2 or a2 <= b1 <= b2:
                    to_add.add((min(a1, a2), max(b1, b2)))
                    to_remove.add(r1)
                    to_remove.add(r2)
                    changed = True
        ranges.difference_update(to_remove)
        ranges.update(to_add)
    fresh = 0
    for a, b in ranges:
        fresh += (b - a) + 1
    ans = fresh
    print(ans)
    return ans


task1()
task2()
