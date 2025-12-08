from util import *
from collections import *
import copy
from functools import reduce
from math import prod, sqrt

day = 8


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    boxes = set()
    distances = []
    box_to_circuit = {}
    for line in data:
        p = tuple([int(e) for e in line.split(",")])
        x, y, z = p
        for box in boxes:
            x1, y1, z1 = box
            d = sqrt((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2)
            distances.append((d, p, box))
        boxes.add(p)
        box_to_circuit[p] = {p}
    distances.sort()
    combines = 1000
    for i in range(combines):
        d, b1, b2 = distances[i]
        c1 = box_to_circuit[b1]
        c2 = box_to_circuit[b2]
        new_circuit = c1.union(c2)
        for box in new_circuit:
            box_to_circuit[box] = new_circuit
    circuits = set([frozenset(s) for s in box_to_circuit.values()])
    circuit_lengths = sorted([len(c) for c in circuits], reverse=True)
    ans = prod(circuit_lengths[:3])
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    boxes = set()
    distances = []
    box_to_circuit = {}
    for line in data:
        p = tuple([int(e) for e in line.split(",")])
        x, y, z = p
        for box in boxes:
            x1, y1, z1 = box
            d = sqrt((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2)
            distances.append((d, p, box))
        boxes.add(p)
        box_to_circuit[p] = frozenset({p})
    distances.sort()

    b1 = (-1, -1, -1)
    b2 = (-1, -1, -1)
    for i in range(len(distances)):
        d, b1, b2 = distances[i]
        c1 = box_to_circuit[b1]
        c2 = box_to_circuit[b2]
        new_circuit = c1.union(c2)
        for box in new_circuit:
            box_to_circuit[box] = new_circuit
        circuits = set([frozenset(s) for s in box_to_circuit.values()])
        if len(circuits) == 1:
            break
    ans = b1[0] * b2[0]
    print(ans)
    return ans


task1()
task2()
