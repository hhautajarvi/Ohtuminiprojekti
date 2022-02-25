from src.database import database_connection

class TipRepository:
    def __init__(self, connection):
        self.connection = connection

    def add_tip(self, title, url, description, user_id):
        self.connection.session.execute("INSERT INTO tip (title, url, description, user_id)" \
            " VALUES (:title, :url, :description, :user_id)", {"title":title, "url":url, "description":description, "user_id":user_id})
        self.connection.session.commit()


tip_repository = TipRepository(database_connection)