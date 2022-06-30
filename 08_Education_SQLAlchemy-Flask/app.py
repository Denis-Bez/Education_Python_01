from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# Other database types:
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/mydatabase'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/mydatabase'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://user:password@127.0.0.1:1521/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # To don't showing a error. No matter

db = SQLAlchemy(app)


# class 'Users' represent table 'users' in database
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 'Column' means that 'id' is table field
    email = db.Column(db.String(50), unique=True) # 'String(50)' means that max string lengh must be 50. 'unique=True' means that values must be unique
    psw = db.Column(db.String(500), nullable=True) # 'nullable=True' means that 'psw' should not be empty
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<users {self.id}>'

class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<profiles {self.id}>'

# 'db.create_all' - Command in consol Python create all class and database


@app.route('/')
def index():
    return render_template('index.html', title='Главная')


@app.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        # TODO: Checking input data
        try:
            hash = generate_password_hash(request.form['psw'])
            print(request.form['email'])
            u = Users(email=request.form['email'], psw=hash)
            # Special object 'session' and method 'add'
            db.session.add(u)
            # Save data from 'session' to table (but it's RAM)
            db.session.flush()

            p = Profiles(name=request.form['name'], old=request.form['old'],
                        city=request.form['city'], user_id = u.id)
            db.session.add(p)
            # Save change from RAM to database
            db.session.commit()
        except:
            # Cancel changes if error
            db.session.rollback()
            print('Ошибка добавления в БД')
            


    return render_template('register.html', title='Регистрация')



if __name__ == '__main__':
    app.run(debug=True)