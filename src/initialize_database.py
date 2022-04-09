from database import database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists user;
    ''')
    cursor.execute('''
        drop table if exists tip;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table user (
            id INTEGER NOT NULL PRIMARY KEY, 
            login_name TEXT NOT NULL, 
            password TEXT NOT NULL, 
            name TEXT
        );
    ''')
    cursor.execute('''
        create table tip (
            id INTEGER NOT NULL PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT,
            url TEXT, 
            description TEXT,
            user_id INTEGER NOT NULL REFERENCES user,
            visible BOOLEAN NOT NULL
        );
    ''')

    connection.commit()


def initialize_database():
    connection = database_connection

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
