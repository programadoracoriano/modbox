import sqlite3

class Database:

    def __init__(self):
        """Class constructor"""
        self.conn = sqlite3.connect("modbox.sqlite")
        self.cursor = self.conn.cursor()

    def _optimize_sqlite(self):
        """Database optimization"""
        self.cursor.execute("PRAGMA journal_mode = WAL")
        self.cursor.execute("PRAGMA synchronous = NORMAL")

    def _setup_tables(self, query: str):
        """Function to setup tables"""
        self.cursor.execute(query)


    def execute(self, query, params=()):
        """Function to execute query"""
        try:
            return self.cursor.execute(query, params)
        except sqlite3.Error as e:
            print(f"Error on Database: {e}")

    def close(self):
        """Function to close database"""
        self.conn.commit()
        self.conn.close()