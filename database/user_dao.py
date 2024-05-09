from entities.user import User
from psycopg import Connection


class UserDao:
    def __init__(self, conn: Connection):
        self.conn = conn

    def getUserById(self, id: str):
        pass

    def getAllUsers(self):
        cursor = self.conn.cursor()

        query = 'select id, first_name, last_name, birthdate  from users'
        cursor.execute(query)

        rows = cursor.fetchall()

        users = []
        for row in rows:
            users.append(User(row))

        cursor.close()
        return users

    def createUser(self, user: User):
        pass

    def deleteUserById(self, id: str):
        pass

    def updateById(self, id: str, params: dict):
        # Update query just for the columns that are in params
        query = "update users set "
        where_query = f" where id = {id}"

        updating_values = []
        for key, value in params:
            updating_values.append(f"{key} = '{value}'")

        query += ','.join(updating_values)
        query += where_query

        cursor = self.conn.cursor()
        cursor.execute(query)

