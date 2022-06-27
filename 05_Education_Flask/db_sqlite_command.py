# Separate script for correcting data base and activate sql commands from 'sq_db.sql'
import sqlite3
import os

def main():
    
    try:
        sqlite_connection = sqlite3.connect('flsite.sqlite')
        cursor = sqlite_connection.cursor()

        query = input('Please, input sql query\n')

        cursor.execute(query)
        #cursor.fetchall() # For fetch tuples from table
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Connection error", error)

    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Connection was closed")


if __name__ == "__main__":
    main()

# List sql-query template:

# INSERT INTO test (title, text, time) VALUES ('Kuzya', 'Good cat', '11')
# DELETE FROM test WHERE id = 1;
# DROP TABLE test;
# INSERT INTO mainmenu (title, url) VALUES ('Авторизация', '/login')