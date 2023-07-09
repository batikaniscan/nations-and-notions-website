from province import Province


class Nation:
    name = ''
    global_capital = 0.0
    accumulated_capital = 0.0
    global_manpower = 0.0
    global_consumables = 0.0
    consumption = 0.0
    global_soldiers = 0
    provinces = []
    contracts = []

    def __init__(self, name, global_capital, accumulated_capital, global_manpower, global_consumables, consumption,
                 global_soldiers, provinces, contracts):
        self.name = name
        self.global_capital = global_capital
        self.accumulated_capital = accumulated_capital
        self.global_manpower = global_manpower
        self.global_consumables = global_consumables
        self.consumption = consumption
        self.global_soldiers = global_soldiers
        self.provinces = provinces
        self.contracts = contracts

    def print_nation(self):
        data = f'NATION: name: {self.name}, global capital: {self.global_capital}, accumulated capital: ' \
               f'{self.accumulated_capital}, global manpower: {self.global_capital}, global consumables: ' \
               f'{self.global_capital}, consumption: {self.consumption}'

        return data

    def has_province(self, id):
        self.print_nation()
        for province in self.provinces:
            province.print_province()
            if province.id == id:
                return province
        return None
