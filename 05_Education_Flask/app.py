from turtle import title
from flask import Flask, render_template, redirect, flash, url_for, session, request, abort, g
from config import CONFIG
import sqlite3
import os
from FDataBase import FDataBase
import time
import math

#DATABASE = '/tmp/flsite.sqlite' # Если мы ниже определяем путь к БД, зачем эта строчка?
DEBUG = True
SECRET_KEY = CONFIG['SECRET_KEY']

application = Flask (__name__)

# Create start configuration of application
application.config.from_object(__name__)
application.config.update(dict(DATABASE=os.path.join(application.root_path, 'flsite.sqlite'))) # Redefine path to database


def connect_db():
    # Устанавливаем соединение с базой данных
    conn = sqlite3.connect(application.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    # Create table in database
    db = connect_db()
    with application.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    # Соединение с базой данных, если оно ещё не установлено
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@application.teardown_appcontext # Срабатывает тогда, когда происходит уничтожение контекста приложения
def close_db(error):
    # Disconnect data base, if it was connected
    if hasattr(g, 'link_db'):
        g.link_db.close()


@application.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu = dbase.getMenu(), posts=dbase.getPostsAnonce())


@application.route('/add_post', methods=['POST', 'GET'])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'])
            if not res:
                flash('Ошибка добавления статьи', category='danger')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи. Короткие имя или текст статьи', category='danger')

    return render_template('add_post.html', menu = dbase.getMenu(), title='Добавление статьи')

@application.route('/post/<int:id_post>')
def showPost(id_post):
        db = get_db()
        dbase = FDataBase(db)
        title, post = dbase.getPost(id_post)
        if not title:
            abort(404)
        
        return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)


if __name__ == "__main__":
    application.run(debug=True)