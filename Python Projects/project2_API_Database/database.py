import sqlite3

class DatabaseManager:

    def __init__(self, dataFile):
        self.dataFile = dataFile

    def connect(self):
        try:
            return sqlite3.connect(self.dataFile)

        except FileNotFoundError:
            print(f'File not found......')

    def create_tables(self):
        users_table_query = ("CREATE TABLE IF NOT EXISTS users( id INTEGER PRIMARY KEY, name VARCHAR(100), email VARCHAR(150) UNIQUE, role VARCHAR(50))")
        services_table_query = ("CREATE TABLE  IF NOT EXISTS services ( service_id INTEGER PRIMARY KEY, service_name VARCHAR(100), price FLOAT)")
        bookings_table_query  = ("CREATE TABLE IF NOT EXISTS bookings ( booking_id INTEGER PRIMARY KEY, user_id INT, service_id INT, date TEXT, FOREIGN KEY(user_id) references users(id), FOREIGN KEY(service_id) references services(service_id))")
        self.execute_query(users_table_query, ())
        self.execute_query(services_table_query, ())
        self.execute_query(bookings_table_query, ())


    def execute_query(self,query,params):
        try:
            with self.connect() as file:
                cursor = file.cursor()
                cursor.execute(query, params)
                return True
        except FileNotFoundError:
            print(f'Error: file not found...')
            return None
        except sqlite3.Error as e:
            print(f'Error: SQL lite error...{e}')
            return None


    def fetch_data(self, query, params):
        try:
            with self.connect() as file:
                cursor = file.cursor()
                cursor.execute(query, params)
                rows = cursor.fetchall()
                cols_list = [col[0] for col in cursor.description]
                result_json = [dict(zip(cols_list, row)) for row in rows]
                return result_json # returns json format

        except FileNotFoundError:
            print(f'Error: file not found...')
            return None
        except sqlite3.Error as e:
            print(f'Error: SQL lite error...{e}')
            return None








