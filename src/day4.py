from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 4


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    rolls = set()
    for x, line in enumerate(data):
        for y, c in enumerate(line):
            if c == "@":
                rolls.add((x, y))

    accessible = set()
    for roll in rolls:
        neighbors = get_neighbors(roll)
        neighbor_count = len([n for n in neighbors if n in rolls])
        if neighbor_count < 4:
            accessible.add(roll)
    ans = len(accessible)
    print(ans)
    return ans


def get_neighbors(p: tuple[int, int]):
    x, y = p
    neighbors = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbors.add((x + i, y + j))
    neighbors.remove(p)
    return neighbors


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    rolls = set()
    for x, line in enumerate(data):
        for y, c in enumerate(line):
            if c == "@":
                rolls.add((x, y))

    removed = 0
    accessible = set()
    while len(accessible) > 0 or removed == 0:
        accessible = set()
        for roll in rolls:
            neighbors = get_neighbors(roll)
            neighbor_count = len([n for n in neighbors if n in rolls])
            if neighbor_count < 4:
                accessible.add(roll)
        rolls.difference_update(accessible)
        removed += len(accessible)
    ans = removed
    print(ans)
    return ans


task1()
task2()
