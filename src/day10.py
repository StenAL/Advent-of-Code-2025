from util import *
from collections import *
from itertools import combinations, chain
import copy
from functools import reduce, lru_cache
import heapq
from math import prod
import time

day = 10


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    machines = []
    for line in data:
        line = line.split(" ")
        light_data = line[0].strip("[").rstrip("]")
        lights = tuple(True if c == "#" else False for c in light_data)

        buttons_data = [e.strip("(").rstrip(")") for e in line[1:-1]]
        buttons = [
            [int(e) for e in button_data.split(",")] for button_data in buttons_data
        ]
        machines.append({"lights": lights, "buttons": buttons})

    presses = 0
    for machine in machines:
        dist = {}
        target = machine["lights"]
        light_count = len(target)
        start = (False,) * light_count
        buttons = machine["buttons"]
        q = [start]
        dist[start] = 0
        while target not in dist:
            u = q.pop(0)
            d = dist[u]
            for neighbor in get_neighbors1(u, buttons):
                if neighbor not in dist:
                    dist[neighbor] = d + 1
                    q.append(neighbor)
        presses += dist[target]
    ans = presses
    print(ans)
    return ans


def get_neighbors1(lights, buttons):
    neighbors = []
    for button in buttons:
        neighbor = tuple(e if i not in button else not e for i, e in enumerate(lights))
        neighbors.append(neighbor)
    return neighbors


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    machines = []
    for line in data:
        line = line.split(" ")
        joltages = tuple(int(e) for e in line[-1].strip("{").rstrip("}").split(","))

        buttons_data = [e.strip("(").rstrip(")") for e in line[1:-1]]
        buttons = tuple(
            tuple(int(e) for e in button_data.split(","))
            for button_data in buttons_data
        )
        machines.append({"joltages": joltages, "buttons": buttons})

    ans = 0
    for i, machine in enumerate(machines):
        print(f"{i + 1} / {len(machines)}")
        target = list(machine["joltages"])
        buttons = machine["buttons"]
        start = (None,) * len(buttons)
        buttons_to_levels = {i: b for i, b in enumerate(buttons)}
        levels_to_buttons = defaultdict(set)
        for i, b in enumerate(buttons):
            for level in b:
                levels_to_buttons[level].add(i)
        q = [start]
        best = -1
        steps = 0
        start = time.time()
        while len(q) > 0:
            state = q.pop()
            steps += 1
            if steps % 100000 == 0:
                print(f"{str(state).replace("None", "-")}")

            levels = get_current_levels(state, target, buttons_to_levels)
            deltas = [target[i] - levels[i] for i in range(len(target))]
            if any(d < 0 for d in deltas):
                continue
            if levels == target:
                cost = sum(e for e in state if e is not None)
                best = cost if best == -1 else min(cost, best)
                print(f"found {state} (cost={cost})")
            if best != -1:
                heuristic = h(deltas)
                cost = sum(e for e in state if e is not None)
                if heuristic + cost >= best and best != -1:
                    continue
            neighbors = get_neighbors(
                state, levels, buttons_to_levels, levels_to_buttons, target
            )
            q.extend(neighbors)
        ans += best
        end = time.time()
        print(f"presses={best}, steps={steps}, time={round(end - start, 2)}")

    print(ans)
    return ans


def h(deltas):
    return max(deltas)


def get_current_levels(state, target, buttons_to_levels):
    levels = [0] * len(target)
    for i, n in enumerate(state):
        if n is None:
            continue
        to_increment = buttons_to_levels[i]
        for j in to_increment:
            levels[j] += n
    return levels


def get_neighbors(state, levels, buttons_to_levels, levels_to_buttons, target):
    btns_to_assign = [i for i, s in enumerate(state) if s is None]
    if len(btns_to_assign) == 0:
        return []
    levels_to_valid_buttons = {
        level: levels_to_buttons[level].intersection(btns_to_assign)
        for level in range(len(levels))
        if levels[level] < target[level]
    }
    for level, buttons in levels_to_valid_buttons.items():
        if len(buttons) == 0:
            return []
    for level, buttons in levels_to_valid_buttons.items():
        if len(buttons) == 1:
            btn_index = next(iter(buttons))
            v = target[level] - levels[level]
            new_state = state[:btn_index] + (v,) + state[btn_index + 1 :]
            return [new_state]

    _, b_i = max((len(buttons_to_levels[i]), i) for i in btns_to_assign)
    # b_i = max(btns_to_assign, key=lambda i: len(buttons_to_levels[i]))
    d = min(target[i] - levels[i] for i in buttons_to_levels[b_i])
    neighbors = []
    for v in range(d, -1, -1):
        new_state = state[:b_i] + (v,) + state[b_i + 1 :]
        neighbors.append(new_state)
    return neighbors


task1()
task2()
