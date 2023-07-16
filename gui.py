import streamlit as st
import db_conn


def main():
    st.set_page_config(page_title='Game Window', layout='wide')
    st.header('Hello world')
    conn = db_conn.connect()
    db_conn.read_data(conn)

