# This parent class include method - 'is_authenticated', 'is_active', 'is_anonymous'. And we may delete them from class 'UserLogin'
from flask import url_for
from flask_login import UserMixin


# class for authorized users
class UserLogin(UserMixin):
    
    # Method fills class content (UserLogin) user's content from database, when browser sends a request
    def fromDB(self, user_id, db):
        self.__user = db.getUser(user_id) # 'getUser' gets content current user from database. Method from class 'FDataBase'
        return self
    
    # Call when user authorize. 
    def create(self, user):
        self.__user = user
        return self

    # def is_authenticated(self):
    #     return True
    # def is_active(self):
    #     return True
    # def is_anonymous(self):
    #     return False
    
    def get_id(self):
        return str(self.__user['id'])
    
    def getName(self):
        return self.__user['name'] if self.__user else 'Без имени'

    def getEmail(self): 
        return self.__user['email'] if self.__user else 'Без email'
    

    def getAvatar(self, application):
        img = None
        if not self.__user['avatar']:
            try:
                with application.open_resource(application.root_path + url_for('static', filename='img/default.png'), 'rb') as f:
                    img = f.read()
            except FileNotFoundError as e:
                print('Не найден аватар по умолчанию'+str(e))
        else:
            img = self.__user['avatar']
        
        return img
    

    def verifyExt(self, filename):
        ext = filename.rsplit('.', 1)[1]
        if ext == 'png' or ext == 'PNG':
            return True
        return False