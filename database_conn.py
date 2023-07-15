import pandas

from nation import Nation, Base
# from province import Province
# from contract import Contract
# from effect import Effect
# from character import Character
# from target_stat import TargetStat
# from story import Story

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
