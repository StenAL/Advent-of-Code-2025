from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 11


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    paths = defaultdict(set)
    for line in data:
        inp, out = line.split(": ")
        out = out.split(" ")
        paths[inp].update(out)
    curr = ["you"]
    while not all(e == "out" for e in curr):
        new_curr = []
        for node in curr:
            if node == "out":
                new_curr.append(node)
                continue
            out = paths[node]
            new_curr.extend(out)
        curr = new_curr
    ans = len(curr)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    # data = get_input_for_file("test2")
    edges = defaultdict(set)
    edges_from = defaultdict(set)
    counts = defaultdict(int)
    for line in data:
        inp, neighbors = line.split(": ")
        neighbors = neighbors.split(" ")
        edges[inp].update(neighbors)
        for e in neighbors:
            edges_from[e].add(inp)

    prefixes = ["fft-", "dac-", "fft-dac-", "dac-fft-"]
    start = "svr"
    counts[start] = 1
    q = topo_sort(start, copy.deepcopy(edges), copy.deepcopy(edges_from))
    while len(q) > 0:
        n = q.pop(0)
        neighbors = edges[n]
        for m in neighbors:
            counts[m] += counts[n]
            if n == "fft":
                counts[f"fft-{m}"] += counts[n]
                counts[f"dac-fft-{m}"] += counts["dac-fft"]
            if n == "dac":
                counts[f"dac-{m}"] += counts[n]
                counts[f"fft-dac-{m}"] += counts["fft-dac"]
            for prefix in prefixes:
                counts[prefix + m] += counts[prefix + n]

    ans = 0
    ans = counts["dac-fft-out"] + counts["fft-dac-out"]
    print(ans)
    return ans


def topo_sort(start, edges, edges_from):
    s = [start]
    l = []
    while len(s) > 0:
        n = s.pop(0)
        l.append(n)
        neighbors = edges[n].copy()
        for m in neighbors:
            edges[n].remove(m)
            edges_from[m].remove(n)
            if len(edges_from[m]) == 0:
                s.append(m)
    return l


task1()
task2()
