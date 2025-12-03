from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 3


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    ans = 0
    for line in data:
        line = [int(e) for e in line]
        highest = max(line[:-1])  # exclude last because no second digit can follow
        highest_index = line.index(highest)
        second_highest = max(line[highest_index + 1 :])
        ans += int(str(highest) + str(second_highest))
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    ans = 0
    for line in data:
        line = [int(e) for e in line]
        joltage = []
        digits = 11
        i = 0
        while digits >= 0:
            highest, offset = get_highest_with_remaining_digits(line[i:], digits)
            i += offset
            digits -= 1
            joltage.append(highest)
        joltage = "".join(str(e) for e in joltage)
        ans += int(joltage)
    print(ans)
    return ans


def get_highest_with_remaining_digits(n: list[int], digits: int) -> tuple[int, int]:
    if digits == 0:
        return max(n), 0
    highest = max(n[:-digits])
    i = n.index(highest)
    return highest, i + 1


task1()
task2()
