from enum import Enum


class State(Enum):
    UNEXPLORED = 0
    EXPLORE_PROGRESS = 1
    EXPLORE_COMPLETE = 2
    COLONIZED = 3
    INVADED = 4


state = {'UNEXP': State.UNEXPLORED,
         'EXP_PROG': State.EXPLORE_PROGRESS,
         'EXP_DONE': State.EXPLORE_COMPLETE,
         'COL': State.COLONIZED,
         'INV': State.INVADED}


class Nation:
    def __init__(self, info):
        try:
            self.name = info[0]
            self.global_capital = info[1]
            self.accumulated_capital = info[2]
            self.global_manpower = info[3]
            self.global_consumption = info[4]
            self.consumables = info[5]
            self.global_soldiers = info[6]
            self.luck = info[7]
        except IndexError:
            print('Wrong tuple')

        self.provinces = []
        self.contracts = []

    def __repr__(self):
        return '[N] ' + self.name

    def if_valid(self):
        return not self.name == 'NPC'

    def add_province(self, province):
        self.provinces.append(province)

    def add_contract(self, contract):
        self.contracts.append(contract)


class Province:
    def __init__(self, info):
        try:
            self.name = info[0]
            self.coords = info[1]
            self.owner_name = info[2]
            self.invading_name = info[3]
            self.capital = {'active_resource': info[4], 'resource_cap': info[5]}
            self.manpower = {'active_resource': info[6], 'resource_cap': info[7]}
            self.consumables = {'active_resource': info[8], 'resource_cap': info[9]}
            self.soldiers = info[10]
            self.state = state[info[11]]
            self.cost = info[12]
        except IndexError:
            print('Wrong tuple')

    def __repr__(self):
        return f'[{self.coords}] {self.name}'


class Contract:
    def __init__(self, info):
        try:
            self.name = info[0]
            self.nation1 = info[1]
            self.nation2 = info[2]
            self.description = info[3]
        except IndexError:
            print('Wrong tuple')

        self.effects = []

    def __repr__(self):
        return f'{self.name}'

    def add_effect(self, effect):
        effects = effect.code.split(',')
        effects = [effect.lstrip().rsplit(' ', 1) for effect in effects]
        effects = [{
            'attribute': effect[0],
            'value': int(effect[1])
        } for effect in effects]

        for effect in effects:
            self.effects.append(effect)


class Effect:
    def __init__(self, info):
        try:
            self.id = info[0]
            self.contract = info[1]
            self.code = info[2]
        except IndexError:
            print('Wrong tuple')

    def __repr__(self):
        return f'{self.code}'
