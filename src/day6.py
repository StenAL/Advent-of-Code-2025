from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 6


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    nums = []
    operators = []
    for i, line in enumerate(data):
        line = [e for e in line.split(" ") if e != ""]
        if i == len(data) - 1:
            operators = line
        else:
            nums.append([int(e) for e in line])
    grand_total = 0
    for i, operator in enumerate(operators):
        row_value = 0 if operator == "+" else 1
        for j in range(len(nums)):
            if operator == "+":
                row_value += nums[j][i]
            else:
                row_value *= nums[j][i]
        grand_total += row_value
    ans = grand_total
    print(ans)
    return ans


def task2():
    data = get_raw_input_for_day(day)
    # data = get_raw_input_for_file("test")
    problems = []
    problem = []
    for x in range(len(data[0])):
        acc = []
        for y in range(len(data)):
            c = data[y][x]
            if c.isnumeric():
                acc.append(c)
            if y == len(data) - 1:
                if c != " ":
                    problem.append(c)
                if len(acc) > 0:
                    problem.append(int("".join(acc)))
                else:
                    problems.append(problem)
                    problem = []
    problems.append(problem)
    grand_total = 0
    for problem in problems:
        op = [e for e in problem if e in ["+", "*"]][0]
        nums = [e for e in problem if e != op]
        if op == "+":
            grand_total += sum(nums)
        else:
            grand_total += prod(nums)
    ans = grand_total
    print(ans)
    return ans


task1()
task2()
