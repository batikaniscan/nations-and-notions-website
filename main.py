import streamlit as st
import backend


def make_square_grid(rows):
    # https://towardsdatascience.com/how-to-create-a-grid-layout-in-streamlit-7aff16b94508
    grid = [0] * rows
    for i in range(rows):
        with st.container():
            grid[i] = st.columns(rows)
    return grid


def make_grid(rows):
    # https://towardsdatascience.com/how-to-create-a-grid-layout-in-streamlit-7aff16b94508
    grid = [0] * rows
    for i in range(rows):
        with st.container():
            grid[i] = st.columns(2)
    return grid


st.set_page_config(page_title='Nations and Notions', layout='wide')

# Import nations data
nations = backend.read_nations_data()

# Compute grid size based on number of nations
# number_of_provinces = len(nations) + 1
number_of_provinces = 3

tabs = st.tabs(['Provinces', 'Nations'])

with tabs[0]:
    st.header('Provinces')

    # Create square grid n x n where n is the number of players + 1 (the dm)
    grid = make_square_grid(number_of_provinces)
    for row in range(0, number_of_provinces):
        for column in range(0, number_of_provinces):
            # Iterate over i and j to populate the grid
            id = f'{row + 1}-{column + 1}'

            # Retrieve province with matching id if it exists
            province = backend.find_province_based_on_id(id, nations)

            grid[row][column].subheader(f'{id}.')

            # If province with matching id exists
            if province and province.id == id:
                grid[row][column].text_input(value=province.name, label=f'{id}: Name:', key=f'{id}-name')
                grid[row][column].text_input(value=province.owner_nation, label=f'{id}: Owner Nation:',
                                             key=f'{id}-owner-nation')
                grid[row][column].text_input(value=province.capital, label='Capital:', key=f'{id}-capital')
                grid[row][column].text_input(value=province.manpower, label='Manpower:', key=f'{id}-manpower')
                grid[row][column].text_input(value=province.consumables, label='Consumables:', key=f'{id}-consumables')
                grid[row][column].text_input(value=province.soldiers, label='Soldiers:', key=f'{id}-soldiers')
            else:
                grid[row][column].text_input(value='', label=f'{id}: Name:', key=f'{id}-name')
                grid[row][column].text_input(value='', label=f'{id}: Owner Nation:', key=f'{id}-owner-nation')
                grid[row][column].text_input(value='', label='Capital:', key=f'{id}-capital')
                grid[row][column].text_input(value='', label='Manpower:', key=f'{id}-manpower')
                grid[row][column].text_input(value='', label='Consumables:', key=f'{id}-consumables')
                grid[row][column].text_input(value='', label='Soldiers:', key=f'{id}-soldiers')
            if row < number_of_provinces - 1:
                grid[row][column].divider()
with tabs[1]:
    st.header('Nations')

    number_of_nations = len(nations)

    # Create grid with 2 columns to display the nations
    grid = make_grid(number_of_nations)
    for row in range(0, number_of_nations):
        nation = nations[row]
        if row % 2 == 0:
            with grid[row][0]:
                grid[0][0].subheader(f'{row + 1}.')
                grid[0][0].text_input(value=nation.name, label='Name:', key=f'{row}-name')
                grid[0][0].text_input(value=nation.global_capital, label='Name:', key=f'{row}-global-capital')
                grid[0][0].text_input(value=nation.accumulated_capital, label='Accumulated Capital:',
                                      key=f'{row}-accumulated-capital')
                grid[0][0].text_input(value=nation.global_consumables, label='Global Consumables:',
                                      key=f'{row}-global-consumables')
                grid[0][0].text_input(value=nation.consumption, label='Consumption:', key=f'{row}-consumption')
                grid[0][0].text_input(value=nation.global_soldiers, label='Global Soldiers:',
                                      key=f'{row}-global-soldiers')

                provinces = ''
                for index, province in enumerate(nation.provinces):
                    if index < len(nation.provinces) - 1:
                        provinces = provinces + province.id + ', '
                    else:
                        provinces = provinces + province.id

                grid[0][0].text_input(value=provinces, label='Province(s):',
                                      key=f'{row}-provinces')

                contracts = ''
                for index, contract in enumerate(nation.contracts):
                    if index < len(nation.contracts) - 1:
                        contracts = contracts + contract + ', '
                    else:
                        contracts = contracts + contract

                grid[0][0].text_input(value=contracts, label='Contract(s):',
                                      key=f'{row}-contracts')

                grid[0][0].write(nation.print_nation())
                if row < number_of_nations - 2:
                    grid[0][0].divider()
        else:
            with grid[row][1]:
                grid[0][1].subheader(f'{row + 1}.')
                grid[0][1].text_input(value=nation.name, label='Name:', key=f'{row}-name')
                grid[0][1].text_input(value=nation.global_capital, label='Name:', key=f'{row}-global-capital')
                grid[0][1].text_input(value=nation.accumulated_capital, label='Accumulated Capital:',
                                      key=f'{row}-accumulated-capital')
                grid[0][1].text_input(value=nation.global_consumables, label='Global Consumables:',
                                      key=f'{row}-global-consumables')
                grid[0][1].text_input(value=nation.consumption, label='Consumption:', key=f'{row}-consumption')
                grid[0][1].text_input(value=nation.global_soldiers, label='Global Soldiers:',
                                      key=f'{row}-global-soldiers')

                provinces = ''
                for index, province in enumerate(nation.provinces):
                    if index < len(nation.provinces) - 1:
                        provinces = provinces + province.id + ', '
                    else:
                        provinces = provinces + province.id

                grid[0][1].text_input(value=provinces, label='Province(s):',
                                      key=f'{row}-provinces')

                contracts = ''
                for index, contract in enumerate(nation.contracts):
                    if index < len(nation.contracts) - 1:
                        contracts = contracts + contract + ', '
                    else:
                        contracts = contracts + contract

                grid[0][1].text_input(value=contracts, label='Contract(s):',
                                      key=f'{row}-contracts')

                grid[0][1].write(nation.print_nation())
                if row < number_of_nations - 2:
                    grid[0][1].divider()
