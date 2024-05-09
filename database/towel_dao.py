from entities.towel import Towel
from psycopg import Connection


class TowelDao:
    def __init__(self, conn: Connection):
        self.conn = conn

    def getById(self, id: str):
        pass

    def getAll(self):
        pass

    def create(self, towel: Towel):
        pass

    def deleteById(self, id: str):
        pass

    def updateById(self, id: str, params: dict):
        # Update query just for the columns that are in params
        query = "update towels set "
        where_query = f" where id = {id}"

        updating_values = []
        for key, value in params:
            updating_values.append(f"{key} = '{value}'")

        query += ','.join(updating_values)
        query += where_query

        cursor = self.conn.cursor()
        cursor.execute(query)

