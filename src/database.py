import sqlite3

database_connection = sqlite3.connect("master.db", check_same_thread=False)
database_connection.isolation_level = None
database_connection.row_factory = sqlite3.Row