from sqlalchemy import Column, Integer, String, REAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Nation(Base):
    __tablename__ = 'nations'

    name = Column('name', String, primary_key=True)
    g_capital = Column('g_capital', Integer)
    a_capital = Column('a_capital', Integer)
    g_manpower = Column('g_manpower', Integer)
    g_consumables = Column('g_consumables', Integer)
    consumption = Column('consumption', REAL)
    g_soldiers = Column('g_soldiers', Integer)

    def __init__(self, name: str = None, g_capital: int = None, a_capital: int = None, g_manpower: int = None,
                 g_consumables: int = None, consumption: float = None, g_soldiers: int = None):
        if name is None:
            # DEFAULT VALUES
            self.name = ''
            self.g_capital = 0
            self.a_capital = 0
            self.g_manpower = 0
            self.g_consumables = 0
            self.consumption = 0.0
            self.g_soldiers = 0
        else:
            self.name = name
            self.g_capital = g_capital
            self.a_capital = a_capital
            self.g_manpower = g_manpower
            self.g_consumables = g_consumables
            self.consumption = consumption
            self.g_soldiers = g_soldiers
        # self.provinces = provinces
        # self.contracts = contracts

    def __repr__(self):
        header = 'name, global capital, accumulated capital, global manpower, global consumables, consumption, ' \
                 'global soldiers'
        base_nation = f'{self.name},{self.g_capital},{self.a_capital},{self.g_manpower},{self.g_consumables},' \
                      f'{self.consumption},{self.g_soldiers}'

        # iterate over provinces and contracts
        # for province in self.provinces:
        #     str_province = province.__str__()
        #     base_nation += str_province

        # for contract in self.contracts:
        #     str_contract = contract.__str__()
        #     base_nation += str_contract
        return header + '\n' + base_nation
