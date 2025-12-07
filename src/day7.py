from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 7


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    splitters = defaultdict(set)
    start = (-1, -1)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            elif c == "^":
                splitters[y].add(x)
    beams = {start[0]}
    rows = len(data)
    splits = 0
    for y in range(rows):
        for splitter in splitters[y]:
            if splitter in beams:
                splits += 1
                beams.remove(splitter)
                beams.add(splitter + 1)
                beams.add(splitter - 1)
    ans = splits
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    splitters = set()
    start = (-1, -1)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "S":
                start = (x, y)
            elif c == "^":
                splitters.add((x, y))
    rows = len(data)
    memo = {start: 1}
    timelines = 0
    for x in range(len(data[0])):
        goal = dp((x, rows - 1), splitters, memo)
        timelines += goal

    ans = timelines
    print(ans)
    return ans


def dp(p, splitters, memo):
    if p in memo:
        return memo[p]
    x, y = p
    if y == 0:
        return 0
    v = 0
    up = (x, y - 1)
    if up not in splitters:
        v += dp((x, y - 1), splitters, memo)
    left = (x - 1, y)
    if left in splitters:
        v += dp(left, splitters, memo)
    right = (x + 1, y)
    if right in splitters:
        v += dp(right, splitters, memo)
    memo[p] = v
    return v


task1()
task2()
