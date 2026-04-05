from database import DatabaseManager
import sqlite3

class InvalidEntry(Exception):
    pass

class BookingManager:
    def __init__(self, database):
        self.database = database

    def get_user_bookings(self):
        try:
            query = 'SELECT * FROM bookings'
            result = self.database.fetch_data(query, ())
            if len(result) == 0: #empty file
                raise InvalidEntry("Error: No bookings yet...")
            else:
                return result
        except InvalidEntry:
            print("No Bookings....")
            return None

    def create_booking(self, user_id, service_id, date):
        try:
            query = f"INSERT INTO bookings(user_id, service_id, date) VALUES (?, ?, ?)"
            params = (user_id, service_id, date)
            self.database.execute_query(query,params)
            return True

        except sqlite3.Error as e:
            print(f'Error: SQL lite error...{e}')
            return None
