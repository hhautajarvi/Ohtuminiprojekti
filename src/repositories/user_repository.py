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

    def get_user(self, username):
        cursor = self.connection.cursor()
        sql = "SELECT login_name FROM user WHERE login_name=:username"
        result = cursor.execute(sql, {"username":username})
        user = result.fetchone()
        if user == None:
            return False
        else:
            return True
    def check_password(self, username, password):
        cursor=self.connection.cursor()
        sql = "SELECT password FROM user WHERE login_name=:login_name and password=:password"
        result = cursor.execute(sql, {"login_name":username, "password":password})
        password = result.fetchone()
        if password == None:
            return False
        return True

user_repository = UserRepository(database_connection)