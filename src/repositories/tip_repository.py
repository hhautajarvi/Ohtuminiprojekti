from src.database import database_connection

class TipRepository:
    def __init__(self, connection):
        self.connection = connection

    def add_tip(self, title, url, description, user_id):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tip (url, description, user_id, title)" \
            " VALUES (?, ?, ?, ?)", (url, description, user_id, title))
        self.connection.commit()


tip_repository = TipRepository(database_connection)