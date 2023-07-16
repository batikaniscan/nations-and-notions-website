import streamlit as st


def connect():
    conn = st.experimental_connection('nations_db', 'sql')
    st.write(conn)
    return conn


def read_data(conn):
    with conn.session as s:
        st.markdown(f"Note that `s` is a `{type(s)}`")
        s.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
        s.execute('DELETE FROM pet_owners;')
        pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
        for k in pet_owners:
            s.execute(
                'INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);',
                params=dict(owner=k, pet=pet_owners[k])
            )
        s.commit()

        pet_owners = conn.query('select * from pet_owners')
        st.dataframe(pet_owners)
