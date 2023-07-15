import database_conn
from nation import Nation

nations = database_conn.alchemy()


def add_new_nation(nation):
    nations.append(nation)
    database_conn.save_nation(nation)

