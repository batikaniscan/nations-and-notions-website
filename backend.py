import pandas as pa
from nation import Nation
from province import Province

data_folder = 'data'
nations_filename = data_folder + '\\' + 'nations.csv'
provinces_filename = data_folder + '\\' + 'provinces.csv'

nations = []


def read_provinces_data():
    df = pa.read_csv(provinces_filename)
    local_provinces = {}

    for index, row in df.iterrows():
        # string type
        id = row['id']
        name = row['name']

        owner_nation = row['owner nation']
        capital = row['capital']
        manpower = row['manpower']
        consumables = row['consumables']
        soldiers = row['soldiers']

        province = Province(id=id, name=name, owner_nation=owner_nation, capital=capital, manpower=manpower,
                            consumables=consumables, soldiers=soldiers)

        if owner_nation in local_provinces:
            local_provinces[owner_nation].append(province)
        else:
            local_provinces[owner_nation] = [province]

    return local_provinces


def read_nations_data():
    df = pa.read_csv(nations_filename, keep_default_na=False)
    local_nations = []
    all_provinces = read_provinces_data()
    provinces = []

    for index, row in df.iterrows():
        # string type
        name = row['name']

        # float values
        global_capital = row['global capital']
        accumulated_capital = row['accumulated capital']
        global_manpower = row['global manpower']
        global_consumables = row['global consumables']
        consumption = row['consumption']
        global_soldiers = row['global soldiers']

        # contracts array type
        contracts = str(row['contracts'])
        # Empty or a single item
        if len(contracts) == 0:
            contracts = ['']
        else:
            contracts = contracts.split(',')

        # Select relevant provinces from all_provinces
        try:
            provinces = all_provinces[name]
        except KeyError:
            print('L BOZO this nation has no provinces')

        nation = Nation(name=name, global_capital=global_capital, accumulated_capital=accumulated_capital,
                        global_manpower=global_manpower, global_consumables=global_consumables, consumption=consumption,
                        global_soldiers=global_soldiers, provinces=provinces, contracts=contracts)
        local_nations.append(nation)
    return local_nations


def print_nations(nations):
    for nation in nations:
        nation.print_nation()
        for province in nation.provinces:
            province.print_province()


def find_province_based_on_id(id, nations):
    # Either provide the province or None
    for nation in nations:
        province = nation.has_province(id)
        if province:
            return province
    return None






def init_session():
    print('Starting session')
    # Read csv files

    # Initialize datatypes
    nations = read_nations_data()
    print_nations(nations)

    # Other session begin activities
    return nations


if __name__ == "__main__":
    # Test
    print('backend.py')
    nations = init_session()

    print('tests')
    test_id = '1-3'
    province = find_province_based_on_id(test_id, nations)
    if province:
        print(province.print_province())
    else:
        print('no provinces')
