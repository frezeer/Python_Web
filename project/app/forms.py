from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField , BooleanField ,TextAreaField
from wtforms.fields.html5 import EmailField

from .models import User

#validaciones manuales apartir de cadenas o strings
def frezeer_validator(form, field):
    if field.data == 'frezee13' or field.data == 'FREZEE13':
        raise validators.ValidationError('El username no es permitido')

class LoginForm(Form):
    username = StringField('Username',[
        validators.length(min=4, max=50, message='El username se encuentra fuera de rango'),
        validators.Required('El usuario es Requerido')
    ])
    password = PasswordField('Password',[
        validators.Required('El password es Requerido')
    ])

class RegisterForm(Form):
    username = StringField('Nombre Usuario', [
        validators.length(min=4 , max=50),
        validators.Required(message='El Usuario es Requerido.'),
        frezeer_validator
    ])
    email = EmailField('Correo Electronico', [
        validators.length(min=6, max=100),
        validators.Required(message='Email es Requerido.'),
        #validators.Email(message='Ingrese un email Valido')
        #raise Exception("Install 'email_validator' for email validation support.")
        #Exception: Install 'email_validator' for email validation support.
    ])
    password = PasswordField('Password',[
            validators.Required('El password es Requerido'),
            validators.EqualTo('confirm_password', message='no coinciden los passwords')
    ])
    confirm_password = PasswordField('Confirmar password')
    accept = BooleanField('', [
        validators.DataRequired(message='Ser Requiere Aceptar los Terminos.')
    ])

    #validaciones desde la base de datos atravez de metodos
    def validate_username(self, username):
        if User.get_by_username(username.data):
             raise validators.ValidationError('El username ya se encuentra en uso')

    def validate_email(self, email):
        if User.get_by_email(email.data):
              raise validators.ValidationError('El email ya esta registrado')

    #sobre escribiendo validate para crea nuestras propias validaciones
    def validate(self):
        if not Form.validate(self):
            return False
        if len(self.password.data) < 3:
            self.password.errors.append('El password es demasiado corto')
            return False

        return True

class TaskForm(Form):
        title = StringField('Titulo',[
            validators.length(min=4, max=50, message='Titulo fuera de rango.'),
            validators.DataRequired(message='El titulo Requerido')
            ])
        description = TextAreaField('Descripcion',[
            validators.DataRequired(message='La Descripcion es Requerida')
        ], render_kw={'rows': 5})
