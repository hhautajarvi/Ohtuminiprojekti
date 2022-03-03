from database import database_connection

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def add_user(self, login_name, password, name):
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO user (login_name, password, name)" \
                " VALUES (?, ?, ?)", (login_name, password, name))
            self.connection.commit()
        except:
            return False       
        return True

user_repository = UserRepository(database_connection)