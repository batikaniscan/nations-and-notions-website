import pandas

from nation import Nation, Base
from province import Province
from contract import Contract
from effect import Effect
from character import Character
from target_stat import TargetStat
from story import Story

import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


def alchemy():
    # nation = Nation('The Island Folk', 70, 204, 40, 72, 60, 0)
    # session.add(nation)
    # session.commit()

    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(Nation).all()
    session.close()
    # st.write(type(results[0]))
    return results


def save_nation(new_nation):
    session = Session()
    session.add(new_nation)
    session.commit()


def update_nation(nation_to_update: Nation):
    st.write(nation_to_update)


def create():
    # Nation 1
    province1_3 = Province(code='1-3', name='The Great Sea', nation='The Island Folk', capital=68 / 100,
                           manpower=36 / 100, consumables=70 / 100, soldiers=0, discovered=1)
    province2_3 = Province(code='2-3', name='Candy Land', nation='The Island Folk', capital=13 / 34,
                           manpower=4 / 18, consumables=12 / 89, soldiers=0, discovered=1)
    contract1 = Contract(nations=('The Island Folk', 'NPC'),
                         title='Candyland of the free? MORE LIKE LAND OF DRUGS AND OBESITY, AMIRIGHT?!',
                         lore='Dayum, so much obesity, so much drug :/', effects=[
            Effect(code='Ca-11', target_stat=TargetStat.CAPITAL, amount=-11.0),
            Effect(code='GCo-10', target_stat=TargetStat.G_CONSUMABLES, amount=-10.0),
            Effect(code='Co+20', target_stat=TargetStat.CONSUMPTION, amount=+20.0)
        ])
    # nation1 = Nation(name='The Island Folk', g_capital=70, a_capital=204, g_manpower=40, g_consumables=72,
    #                 consumption=60.0, g_soldiers=0, provinces=[province1_3, province2_3], contracts=[contract1])

    # Nation 2
    province2_1 = Province(code='2-1', name='Dragon\'s Hope', nation='Constelia', capital=85 / 100,
                           manpower=32 / 100, consumables=31 / 100, soldiers=2, discovered=1)
    province3_1 = Province(code='2-1', name='Deeprains Jungle', nation='Constelia', capital=10 / 85,
                           manpower=14 / 58, consumables=15 / 96, soldiers=2, discovered=1)

    contract2 = Contract(nations=('Dragon\'s Hope', 'NPCs'), title='Sacrificial Lamb',
                         lore='Under a lucky star, a dragon (Lacona) of Dragons Hope discovered a barbarian '
                              'folk (through Gunknacks arrow accident). They started worshiping the dragons of '
                              'Constelia as Gods and now regularly offer them food.',
                         effects=Effect(code='Co+10', target_stat=TargetStat.CONSUMABLES, amount=3.0))
    contract3 = Contract(nations=('Constelia', 'Mysterious Tower in the Mouth of Hell'), title='Dark Lord’s Gloom',
                         lore='In one of the biggest mountains of Dragon’s Hope opened up and revealed an ancient evil:'
                              'In a sea of magma, there stands one tower tall, reaching into the sky. It exhibits a'
                              'negative aura, damaging the people’s will to work.',
                         effects=Effect(code='Ca-10', target_stat=TargetStat.CAPITAL, amount=-10.0))

    # nation2 = Nation(name='Constelia', g_capital=85, a_capital=151, g_manpower=46, g_consumables=49,
    #                  consumption=46.2, g_soldiers=2, provinces=[province2_1, province3_1], contracts=[
    #        contract2, contract3
    #   ])

    # print(nation1)
    #   print(nation2)

    character = Character(name='Gungnack', pronouns=['He', 'Him', 'Plush'],
                          lore='Son of the barbarian chief. Brave and foolish.')

    print(character)

    story = Story(events=['A group of space dragons who rebel against their xenophobic kind traveled to this land to '
                          'establish a permanent base for their revolution. They chose a mountain range as their '
                          'primary location and called their new settlement Dragons Hope. '
                          'Their nation is known as Constelia.',
                          'At first they struggled finding enough food to feed their enormous nutritional needs. '
                          'After establishing contact with native inhabitants and trade relations with the people '
                          'of the sea though, they overcame the initial famine.'])

    print(story)


if __name__ == '__main__':
    db_pop()
