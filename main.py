import backend
import database_conn
from nation import Nation

import streamlit as st

st.set_page_config(page_title='Nations and Notions', layout='wide')

tab_nations, tab_provinces, tab_characters, tab_story = st.tabs(['Nations', 'Provinces', 'Characters', 'Story'])
with tab_nations:
    database_conn.alchemy()
    nations = backend.nations

    st.header('NATIONS')
    expander = st.expander('Add new nation')
    with expander:
        with st.form('new-nation-form', clear_on_submit=True):
            new_nation_name = st.text_input('Name:', value='', key='new_nation_name')
            new_nation_g_capital = st.text_input('Global Capital:', value=0, key='new_nation_g_capital')
            new_nation_a_capital = st.text_input('Accumulated Capital:', value=0, key='new_nation_a_capital')
            new_nation_g_manpower = st.text_input('Global Manpower:', value=0, key='new_nation_g_manpower')
            new_nation_g_consumables = st.text_input('Global Consumables:', value=0, key='new_nation_g_consumables')
            new_nation_consumption = st.text_input('Consumption:', value=0.0, key='new_nation_consumption')
            new_nation_g_soldiers = st.text_input('Global soldiers:', value=0, key='new_nation_g_soldiers')

            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                new_nation = Nation(name=new_nation_name, g_capital=new_nation_g_capital,
                                    a_capital=new_nation_a_capital, g_manpower=new_nation_g_manpower,
                                    g_consumables=new_nation_g_consumables, consumption=new_nation_consumption,
                                    g_soldiers=new_nation_g_soldiers)
                backend.add_new_nation(new_nation)

    col1, col2 = st.columns(2)

    with col1:
        for index, nation in enumerate(nations):
            if index % 2 == 0:
                with st.container():
                    st.text_input('Name:', value=nation.name, key=f'{index}name')
                    st.text_input('Global Capital:', value=nation.g_capital, key=f'{index}g_capital')
                    st.text_input('Accumulated Capital:', value=nation.a_capital, key=f'{index}a_capital')
                    st.text_input('Global Manpower:', value=nation.g_manpower, key=f'{index}g_manpower')
                    st.text_input('Global Consumables:', value=nation.g_consumables, key=f'{index}g_consumables')
                    st.text_input('Consumption:', value=nation.consumption, key=f'{index}consumption')
                    st.text_input('Global soldiers:', value=nation.g_soldiers, key=f'{index}g_soldiers')
                st.divider()
    with col2:
        for index, nation in enumerate(nations):
            if index % 2 != 0:
                with st.container():
                    st.text_input('Name:', value=nation.name, key=f'{index}name')
                    st.text_input('Global Capital:', value=nation.g_capital, key=f'{index}g_capital')
                    st.text_input('Accumulated Capital:', value=nation.a_capital, key=f'{index}a_capital')
                    st.text_input('Global Manpower:', value=nation.g_manpower, key=f'{index}g_manpower')
                    st.text_input('Global Consumables:', value=nation.g_consumables, key=f'{index}g_consumables')
                    st.text_input('Consumption:', value=nation.consumption, key=f'{index}consumption')
                    st.text_input('Global soldiers:', value=nation.g_soldiers, key=f'{index}g_soldiers')
                st.divider()
