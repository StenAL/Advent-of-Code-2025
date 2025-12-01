from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 1


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    current = 50
    zeros = 0
    for line in data:
        dir = line[0]
        amt = int(line[1:])
        if dir == "L":
            amt = -amt
        current += amt
        if current % 100 == 0:
            zeros += 1
    ans = zeros
    print(ans)


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    current = 50
    zeros = 0
    for line in data:
        dir = line[0]
        prev = current - 1 if dir == "L" else current + 1
        amt = int(line[1:])
        if dir == "L":
            amt = -amt
        current += amt
        ends = sorted([prev, current])
        passed_nums = range(ends[0], ends[1] + 1)
        zeros += len([n for n in passed_nums if n % 100 == 0])
    ans = zeros
    print(ans)


task1()
task2()
