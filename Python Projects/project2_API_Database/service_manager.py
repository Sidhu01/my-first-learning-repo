from database import DatabaseManager
import sqlite3

class InvalidEntry(Exception):
    pass

class ServiceManager:
    def __init__(self, database):
        self.database = database

    def list_services(self):
        try:
            query = 'SELECT * FROM services'
            result = self.database.fetch_data(query, ())
            if len(result) == 0: #empty file
                raise InvalidEntry("Error: File is empty, please add services...")
            else:
                return result
        except InvalidEntry:
            print("Error: Empty file....")
            return None

    def add_service(self, name, price):
        try:
            query = "INSERT INTO services(service_name, price) VALUES (?, ?)"
            params = (name, price)
            self.database.execute_query(query, params)
            return True

        except sqlite3.Error as e:
            print(f'Error: SQL lite error...{e}')
            return None
