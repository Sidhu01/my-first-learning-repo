from database import DatabaseManager
import sqlite3
import re

class InvalidEntry(Exception):
    pass

class UserService:

    def __init__(self, database):
        self.database = database

    def get_users(self):
        try:
            query = 'SELECT * FROM users'
            result = self.database.fetch_data(query, ())
            if len(result) == 0: #empty file
                raise InvalidEntry("Error: File is empty, please add users...")
            else:
                return result
        except InvalidEntry:
            print("Error: Empty file....")
            return None


    def create_user(self, name, email, role):
        try:
            if not re.match('^[^@]+@[^@]+.[^@]+$', email):
                raise InvalidEntry("Error: Please check your email")
            query = f"INSERT INTO users(name, email, role) VALUES (?, ?, ?)"
            params = (name, email, role)
            self.database.execute_query(query, params)
            return True

        except sqlite3.Error as e:
            print(f'Error: SQL lite error...{e}')
            return None
        except InvalidEntry:
            print("Error: Please check your email")
            return None


    def delete_user(self, user_id):
        try:

            if user_id is None:
                query = "DELETE FROM users WHERE id IS NULL"
                params = ()
                self.database.execute_query(query, params)
            else:
                query = " DELETE FROM users WHERE id = ?"
                params = (int(user_id),)
                self.database.execute_query(query, params)
            return True

        except sqlite3.Error as e:
            print(f'Error: SQL lite error...{e}')
            return None


    def update_user(self, user_id, name, email, role):
        try:
            if not re.match('^[^@]+@[^@]+.[^@]+$', email):
                raise InvalidEntry("Error: Please check your email")
            query = f"UPDATE users SET name = ?, email = ?, role = ? WHERE id = ?"
            params = (name, email, role, int(user_id))
            self.database.execute_query(query, params)
            return True

        except sqlite3.Error as e:
            print(f'Error: SQL lite error...{e}')
            return None
        except InvalidEntry:
            print("Error: Please check your email")
            return None

