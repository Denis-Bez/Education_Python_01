from datetime import datetime
from flask import Flask, make_response, render_template, redirect, flash, url_for, session, request, abort, g, make_response
from config import CONFIG
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os
from FDataBase import FDataBase
import time
import math
import datetime

#DATABASE = '/tmp/flsite.sqlite' # What for? 
DEBUG = True
SECRET_KEY = CONFIG['SECRET_KEY']

application = Flask (__name__)

# Create start configuration of application
application.config.from_object(__name__)
application.config.update(dict(DATABASE=os.path.join(application.root_path, 'flsite.sqlite'))) # Redefine path to database
# application.permanent_session_lifetime = datetime.timedelta(days=10) # To set custom session livetime


def connect_db():
    # Connecting with database
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
    # Connection with data base if it was not connected
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


dbase = None
# Connect with database before request
# Fuck! It's connected many times
@application.before_request
def before_request():

    # Was - in each handler:
    # db = get_db()
    # dbase = FDataBase(db)
    global dbase
    db = get_db()
    dbase = FDataBase(db)


@application.teardown_appcontext # Срабатывает тогда, когда происходит уничтожение контекста приложения
def close_db(error):
    # Disconnect data base, if it was connected
    if hasattr(g, 'link_db'):
        g.link_db.close()


@application.route('/')
def index():
    return render_template('index.html', menu = dbase.getMenu(), posts=dbase.getPostsAnonce())


@application.route('/add_post', methods=['POST', 'GET'])
def add_post():

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добавления статьи', category='danger')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи. Короткие имя или текст статьи', category='danger')

    return render_template('add_post.html', menu = dbase.getMenu(), title='Добавление статьи')

# Page of post
@application.route('/post/<alias>')
def showPost(alias):
        title, post = dbase.getPost(alias)
        if not title:
            abort(404)
        
        return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)
    

@application.route('/login')
def login():

    return render_template('login.html', title='Авторизация')


@application.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['email']) > 4\
            and len(request.form['psw']) > 4 and request.form['psw'] == request.form['psw2']:

            hash = generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['name'], request.form['email'], hash)
            if res:
                flash('Вы успешно зарегистрированы', category='success')
                return redirect(url_for('login'))
            else:
                flash('Ошибка при добавлении в БД', category='danger')
        else:
            flash('Неверно заполнены поля', category='danger')

    return render_template('register.html', title='Регистрация')

# Generate a server response
#@application.route('/lesson_11')
#def lesson_11():

    # # Opportunity using 'make_response' №1
    # content = render_template('index.html', posts=[])
    # # make_response(res_body, status_code=200), where 'res_body' - sending content, 'satatus_code' - server response code
    # res = make_response(content)
    # # display 'index.html' as a regular string
    # res.headers['Content-Type'] = 'text/plain'
    # # optional
    # res.headers['Server'] = 'flasksite'
    # return res

    # Opportunity using 'make_response' №2
    # img = None
    # with application.open_resource(application.root_path + '\static\img\prince1.jpg', mode='rb') as f:
    #     img = f.read()
    # if img is None:
    #     return 'None image'   
    # res = make_response(img)
    # res.headers['Content-Type'] = 'image/jpg' # If write 'text/plain' that browser doesn't show picture
    # return res

    # # Opportunity using 'make_response' №3
    # res = make_response('<h1>Ошибка сервера<h1>', 500)
    # return res

    # Three types server response 1) (response, status, headers) 2) (response, headers) 3) (response, status)
    # @application.errorhandler(404)
    # def pageNot(error):
    #     return ('Страница не найдена', 404)
    # return '<h1>Main Page</h1>', 200, {'Content-Type': 'text/plan'}

    # 302 (temporarily), 301 (permanent) Redurect. Function in Flsk: redirect(location, status)
    # return redirect(url_for('index'), 301)

    # hooking of requests (перехват запросов)
# @application.before_first_request
# def before_first_request():
#     print('before_first_request() called')
# @application.before_request
# def before_request():
#     print('before_request() called')
# @application.after_request
# def after_request(response):
#     print('after_request() called')
#     return response
# @application.teardown_request
# def teardown_request(response):
#     print('teardown_request() called')
#     return response

# Set cookies. function - set_cookie(key, value='', max_age=None(in seconds))
# No security
# @application.route('/login')
# def login():
#     log = ''
#     if request.cookies.get('logged'):
#         log = request.cookies.get('logged')
    
#     res = make_response(f'<h1>Форма авторизации</h1><p>logged: {log}')
#     # Record information 'yes' on key 'logged'
#     res.set_cookie('logged', 'yes')
#     # return response with cookie
#     return res
# @application.route('/logout')
# def logout():
#     res = make_response('<p>Вы больше не авторизованы!</p>')
#     res.set_cookie('logged', '', 0)
#     return res

# Lesson Session
# Server sending data of session to browser only if object "session" was changed
# @application.route('/session')
# def session_data():
    # if 'visits' in session:
    #     session['visits'] = session.get('visits') + 1
    # else:
    #     session['visits'] = 1
    # return f'<h1>Main Page</h1><p>Число просмотров: {session["visits"]}'


# data = [1, 2, 3, 4]
# @application.route('/session')
# def session_data():
#     session.permanent = False # To we can set livetime session (Default 31 days). This all the time update condition 'session' (when false and when true)

#     if 'data' not in session:
#         session['data'] = data
#     else:
#         session['data'][1] += 1
#         # session.modified = True # so that Falsk can see changing condition object 'session'
    
#     return f'<p>session["data"]: {session["data"]}'


if __name__ == "__main__":
    application.run(debug=True)