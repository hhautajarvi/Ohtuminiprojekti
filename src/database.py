import sqlite3
from os import getenv

database_connection = sqlite3.connect(getenv('DATABASE', "not found"), check_same_thread=False)
database_connection.isolation_level = None
database_connection.row_factory = sqlite3.Row
