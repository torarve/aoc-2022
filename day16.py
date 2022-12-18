from common import read_lines
from itertools import permutations
import re

class Node:
    _counter = 0
    def __init__(self, name, flow_rate):
        self.id = Node._counter
        Node._counter += 1
        self.name = name
        self.flow_rate = flow_rate

    def clone(self) -> "Node":
        return Node(self.name, self._flow_rate)
        
    def __repr__(self):
        return f"Node({self.visited},{self.name},{flow_rate})"


lines ="""Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".split("\n")

lines = read_lines("input16.txt")

nodes: list[Node] = []
neighbours: dict[str, list[str]] = {}
cost: dict[dict[int]] = {}

for line in lines:
    m = re.match(r"Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line)
    name, flow_rate, adjacent = m.groups()
    flow_rate = int(flow_rate)
    adjacent = adjacent.split(", ")
    neighbours[name] = adjacent
    nodes. append(Node(name, flow_rate))

for node in nodes:
    cost[node.name] = {}
    w = 1
    current = [node.name]
    while len(current)>0:
        working_set = [x for node_name in current for x in neighbours[node_name] if x not in cost[node.name] and x!=node.name]
        for next in working_set:
            cost[node.name][next] = min(w, cost[node.name].get(next, w))
        
        current = working_set
        w += 1


states = {v.name: 1 << i for i,v in enumerate([x for x in nodes if x.flow_rate>0])}

def visit(nodes, name: str, state: int, flow: int, time_remaining:int, answer):
    answer[state] = max(answer.get(state, 0), flow)
    for next in [x for x in nodes if x.name != name and x.flow_rate>0]: # nodes:
        minutes = time_remaining - cost[name][next.name] - 1

        if (states[next.name] & state) or minutes <=0:
            continue
        answer = visit(nodes, next.name, states[next.name] | state, flow + (minutes*next.flow_rate), minutes, answer)

    return answer

part1 = visit([x for x in nodes if x.flow_rate>0], "AA", 0, 0, 30, {})
print(max(part1.values()))
part2 = visit([x for x in nodes if x.flow_rate>0], "AA", 0, 0, 26, {})
print(max((val1+val2)
    for k1, val1 in part2.items() 
    for k2, val2 in part2.items() 
    if not (k1 & k2)))
