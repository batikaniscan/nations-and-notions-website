class Province:
    id = ''
    name = ''
    owner_nation = ''
    capital = ''
    manpower = ''
    consumables = ''
    soldiers = 0

    def __init__(self, id, name, owner_nation, capital, manpower,
                 consumables, soldiers):
        self.id = id
        self.name = name
        self.owner_nation = owner_nation
        self.capital = capital
        self.manpower = manpower
        self.consumables = consumables
        self.soldiers = soldiers

    def print_province(self):
        data = f'PROVINCE: id: {self.id}, name: {self.name}, owner nation: {self.owner_nation}, capital: ' \
               f'{self.capital}, manpower: {self.manpower}, consumables: {self.consumables}, soldiers: {self.soldiers}'
        return data


