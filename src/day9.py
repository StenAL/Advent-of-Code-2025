from util import *
from collections import *
import copy
import itertools
from functools import reduce
from math import prod

day = 9


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    tiles = []
    for line in data:
        tiles.append([int(e) for e in line.split(",")])
    pairs = itertools.combinations(tiles, 2)
    areas = []
    for a, b in pairs:
        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        areas.append(area)
    largest_area = max(areas)
    ans = largest_area
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    tiles = []
    tiles_rows = defaultdict(set)
    for i, line in enumerate(data):
        prev = data[(i - 1) % len(data)]
        prev_x, prev_y = [int(e) for e in prev.split(",")]
        x, y = [int(e) for e in line.split(",")]
        x_min, x_max = sorted([x, prev_x])
        y_min, y_max = sorted([y, prev_y])
        tiles.append((x, y))
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                tiles_rows[y].add(x)

    tiles_rows = {k: sorted(v) for k, v in tiles_rows.items()}
    pairs = list(itertools.combinations(tiles, 2))
    areas = []
    for i, pair in enumerate(pairs):
        print(f"{i + 1}/{len(pairs)}")
        a, b = pair
        x_min, x_max = sorted([a[0], b[0]])
        y_min, y_max = sorted([a[1], b[1]])
        is_valid = True
        for y in range(y_min, y_max + 1):
            row = tiles_rows[y]
            if x_min < row[0]:
                is_valid = False
                break
            if x_max > row[-1]:
                is_valid = False
                break

        if not is_valid:
            continue

        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        areas.append(area)
    largest_area = max(areas)
    ans = largest_area
    print(ans)
    return ans


task1()
task2()
