from common import read_lines
import re

class Blueprint:
    def __init__(self, id):
        self.id = id
        self.lines: dict[str,dict[str,int]] = {}

    def __repr__(self):
        return f"Blueprint({self.id})"

lines = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".split("\n")

limit = 24
blueprints: list[Blueprint] = []


for line in lines:
    tmp = line.split(": ")
    id = int(tmp[0][10:])
    blueprint = Blueprint(id)
    for tmp2 in tmp[1].split(". "):
        m = re.match(r"Each (\w+) robot costs (.+)", tmp2)
        type = m.group(1)
        costs = dict([(name, int(cost)) 
            for cost, name in [tuple(t.split(" ")) 
                for t in m.group(2).strip(".").split(" and ")]])
        blueprint.lines[type] = costs

    blueprints.append(blueprint)

robots = { "ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
wallet = { "ore": 0, "clay": 0, "obsidian": 0, "geode": 0}

def step(remaining: int, blueprint: Blueprint, robots: dict[str,int], wallet: dict[str,int], seen):
    can_build = []
    state = f"{robots}|{wallet}|{remaining}"
    if state in seen:
        return seen[state]

    geode_line = blueprint.lines["geode"]
    for key, value in wallet.items():
        if key in geode_line and geode_line[key]>value+remaining:
            # Not possible to open any geodes in the remaining time 
            return 0

    if remaining == 0: return wallet["geode"]
    for type, cost in blueprint.lines.items():
        if all([wallet[cost_item]>=cost_value for cost_item, cost_value in cost.items()]):
            # Choose: build or not?
            can_build.append(type)

    for type, count in robots.items():
        wallet[type] += count

    best_value = wallet["geode"]
    for to_build in can_build:
        new_wallet = dict(x for x in wallet.items())
        new_robots = dict(x for x in robots.items())
        for type, value in blueprint.lines[to_build].items():
            new_wallet[type] -= value
        new_robots[to_build] += 1
        if to_build == "geode":
            print(f"Building {to_build} with {remaining} remaining minutes. {wallet}, {robots}")
        best_value = max(best_value, step(remaining-1, blueprint, new_robots, new_wallet, seen))

    best_value = max(best_value, step(remaining-1, blueprint, robots, wallet, seen))
    seen[state] = best_value

    return best_value


for blueprint in blueprints:
    wallet = step(24, blueprint, { "ore": 1, "clay": 0, "obsidian": 0, "geode": 0}, { "ore": 0, "clay": 0, "obsidian": 0, "geode": 0}, {})
    print(wallet)
    # for i in range(0, limit):
    #     can_build = []
    #     for type, cost in blueprint.lines.items():
    #         if all([wallet[cost_item]>=cost_value for cost_item, cost_value in cost.items()]):
    #             # Choose: build or not?
    #             can_build.append(type)

    #     print(i, can_build)

    #     for type, count in robots.items():
    #         wallet[type] += count

    #     print(wallet)

