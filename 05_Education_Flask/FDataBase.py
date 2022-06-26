import sqlite3
import time
import math

from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    # Method returns list of values from table "mainmenu"
    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('Ошибка чтения из БД')
        return [] # If error, it returns empty list
    
    # Method add post to table
    def addPost(self, title, text, url):
        try:
            # Check that 'url' already doesn't exist
            self.__cur.execute(f'SELECT COUNT() as "count" FROM posts WHERE url LIKE "{url}"')
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Статья с таким url уже существует')
                return False

            # time execute
            tm = math.floor(time.time())

            # insert values to table
            self.__cur.execute('INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)', (title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в БД'+str(e))
            return False
        
        return True

    # Get post from table "posts"
    def getPost(self, alias):
        try:
            self.__cur.execute(f'SELECT title, text FROM posts WHERE url LIKE "{alias}" LIMIT 1')
            res = self.__cur.fetchone() # Mehod takes one value
            if res:
                
                # Regular expressions to invite full links to image
                # !!!Better save correcting link to data base for saving resourses
                # base = url_for('static', filename='img')
                # url to image
                # text = re.sub(r'(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>',
                #                 '\\g<tag>' + base + "/\\g<url>>",
                #                 res['text'])
                # return (res['tittle', text])

                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД"+str(e))
        
        return (False, False)
    
    # Getting post annonce
    def getPostsAnonce(self):
        try:
            self.__cur.execute(f'SELECT id, title, text, url FROM posts ORDER BY time DESC')
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print('Ошибка получения статьи из БД'+str(e))
        
        return []