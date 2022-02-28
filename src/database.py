import sqlite3
from os import detenv

database_connection = sqlite3.connect(detenv('DATABASE'), check_same_thread=False)
database_connection.isolation_level = None
database_connection.row_factory = sqlite3.Row