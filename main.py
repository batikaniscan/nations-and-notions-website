import streamlit as st
import backend


def make_grid(rows):
    # https://towardsdatascience.com/how-to-create-a-grid-layout-in-streamlit-7aff16b94508
    grid = [0] * rows
    for i in range(rows):
        with st.container():
            grid[i] = st.columns(rows)
    return grid


st.set_page_config(page_title='Nations and Notions', layout='wide')

st.header('Provinces')
nations = backend.read_nations_data()

# for nation in nations:
#    st.write(nation.print_nation())
#    for province in nation.provinces:
#        st.write(province.print_province())


# Create square table n x n where n is the number of players + 1 (the dm)
number_of_provinces = len(nations) + 1

grid = make_grid(number_of_provinces)
# grid[0][0].write('1-1')

for i in range(0, number_of_provinces):
    for j in range(0, number_of_provinces):
        id = f'{i+1}-{j+1}'
        grid[i][j].header(id)
        province = backend.find_province_based_on_id(id, nations)

        if province and province.id == id:
            grid[i][j].text_input(value=province.name, label='Name:', key=f'{id}-name')
            grid[i][j].text_input(value=province.capital, label='Capital:', key=f'{id}-capital')
            grid[i][j].text_input(value=province.manpower, label='Manpower:', key=f'{id}-manpower')
            grid[i][j].text_input(value=province.consumables, label='Consumables:', key=f'{id}-consumables')
            grid[i][j].text_input(value=province.soldiers, label='Soldiers:', key=f'{id}-soldiers')
        else:
            grid[i][j].text_input(value='', label='Name:', key=f'{id}-name')
            grid[i][j].text_input(value='', label='Capital:', key=f'{id}-capital')
            grid[i][j].text_input(value='', label='Manpower:', key=f'{id}-manpower')
            grid[i][j].text_input(value='', label='Consumables:', key=f'{id}-consumables')
            grid[i][j].text_input(value='', label='Soldiers:', key=f'{id}-soldiers')


        # grid[i][j].header(province.name)
