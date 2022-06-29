from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

# class for input forms in html files
class LoginForm(FlaskForm):
    # 'validators' checking inputing data to form
    email = StringField('Email:', validators=[Email("Некорректный email")])
    psw = PasswordField('Пароль:', validators=[DataRequired(), Length(min=4, max=100, message="Длина пароля должна быть от 4 до 100 символов")])
    remember = BooleanField('Запомнить', default=False) # Checkbox
    submit = SubmitField('Войти')

class RegisterForm(FlaskForm):
    name = StringField('Имя: ', validators=[Length(min=4, max=100, message="Имя должно быть от 4 до 100 символов")])
    email = StringField('Email:', validators=[Email("Некорректный email")])
    psw = PasswordField('Пароль:', validators=[DataRequired(), Length(min=4, max=100, message="Длина пароля должна быть от 4 до 100 символов")])
    # 'EqualTo' check - psw equals psw2
    psw2= PasswordField('Пароль:', validators=[DataRequired(), EqualTo('psw', "Пароли не совпадают"), Length(min=4, max=100, message="Длина пароля должна быть от 4 до 100 символов")])
    submit = SubmitField('Регистрация')