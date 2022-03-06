import sqlite3
import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)
load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
database_connection = sqlite3.connect(os.getenv('DATABASE', "not found"), check_same_thread=False)
database_connection.isolation_level = None
database_connection.row_factory = sqlite3.Row