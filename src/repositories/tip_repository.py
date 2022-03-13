from database import database_connection
from entities.tip import Tip

def get_tip_by_row(row):
    return Tip(row['id'], row['title'], row["author"], row['url'], \
        row['description'], row['user_id'], row['visible']) if row else None

class TipRepository:
    def __init__(self, connection):
        self.connection = connection

    def add_tip(self, title, author, url, description, user_id, visible=1):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tip (title, author, url, description, user_id, visible)" \
            " VALUES (?, ?, ?, ?, ?, ?)", (title, author, url, description, user_id, visible))
        self.connection.commit()

    def get_tips(self):
        """Palauttaa kaikki lukuvinkit listana"""

        cursor = self.connection.cursor()
        sql = """SELECT id, title, author, url, description, user_id, visible FROM Tip"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        return list(map(get_tip_by_row, rows))

    def get_searched_tips(self, query):
        """Palauttaa vinkkien otsikoista haetut tulokset"""

        cursor = self.connection.cursor()
        try:
            sql = """SELECT id, title, author, url, description, user_id FROM Tip WHERE title LIKE :query AND visible=1"""
            cursor.execute(sql, {"query":"%"+query+"%"})
            rows = cursor.fetchall()
        except:
            return []
        return rows

    def hide_tip(self, tip_id):
        """Asettaa lukuvinkkitaulun visible-sarakkeeseen arvon False.
        Metodin avulla voidaan piilottaa haluttu rivi."""

        cursor = self.connection.cursor()
        try:
            sql = """UPDATE Tip SET visible=? WHERE id=?"""
            cursor.execute(sql, (0, tip_id))
            self.connection.commit()
        except:
            return False
        return True

tip_repository = TipRepository(database_connection)
