import sqlite3 as sql
from classes import *

conn = sql.connect('nations_db.db')
cur = conn.cursor()


def create_map(size, provinces=None):
    game_map = []
    for i in range(0, size):
        game_map.append([])
        for j in range(0, size):
            coords = f'{i + 1}-{j + 1}'
            if not provinces:
                game_map[i].append(f'[{coords}]')
            else:
                found = False
                for province in provinces:
                    if province.coords == coords:
                        game_map[i].append(province)
                        found = True
                        continue
                if not found:
                    game_map[i].append(f'[{coords}]')

    return game_map


def print_map(game_map):
    for index, row in enumerate(game_map):
        for col in game_map[index]:
            print(str(col) + ' ', end='')
        print()


def read_nations():
    res = cur.execute('''SELECT * FROM nation''')
    nations = []
    for row in res:
        nation = Nation(row)
        nations.append(nation)
    return nations


def read_provinces():
    res = cur.execute('''SELECT * FROM province''')
    provinces = []
    for row in res:
        province = Province(row)
        provinces.append(province)
    return provinces


def read_contracts():
    res = cur.execute('''SELECT * FROM contract''')
    contracts = []
    for row in res:
        contract = Contract(row)
        contracts.append(contract)
    return contracts


def read_effects():
    res = cur.execute('''SELECT * FROM effect''')
    effects = []
    for row in res:
        effect = Effect(row)
        effects.append(effect)
    return effects


def print_all(cur):
    res = cur.execute('''SELECT * FROM nation''')
    for row in res:
        print(row)
    res = cur.execute('''SELECT * FROM province''')
    for row in res:
        print(row)
    res = cur.execute('''SELECT * FROM contract''')
    for row in res:
        print(row)
    res = cur.execute('''SELECT * FROM effect''')
    for row in res:
        print(row)
    res = cur.execute('''SELECT * FROM character''')
    for row in res:
        print(row)
    res = cur.execute('''SELECT * FROM story''')
    for row in res:
        print(row)


def init():
    conn = sql.connect('nations_db.db')
    cur = conn.cursor()

    nations = read_nations()
    provinces = read_provinces()
    contracts = read_contracts()
    effects = read_effects()

    game_map = create_map(len(nations), provinces)

    for nation in nations:
        if not nation.if_valid():
            continue
        else:
            for province in provinces:
                if nation.name == province.owner_name:
                    nation.add_province(province)
    for contract in contracts:
        for nation in nations:
            if not nation.if_valid():
                continue
            else:
                if contract.nation1 == nation.name or contract.nation2 == nation.name:
                    nation.add_contract(contract)
    for nation in nations:
        if not nation.if_valid():
            continue
        else:
            for contract in nation.contracts:
                for effect in effects:
                    if effect.contract == contract.name:
                        contract.add_effect(effect)

    return nations, game_map



if __name__ == '__main__':
    init()
