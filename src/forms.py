from wtforms import Form
from wtforms import StringField
from wtforms import TextField
from wtforms import PasswordField
from wtforms import HiddenField
from wtforms import IntegerField
from wtforms import FloatField
from wtforms import BooleanField
from wtforms import DateField
from wtforms import validators
from wtforms import TimeField
from wtforms import RadioField
from wtforms import FieldList
from wtforms import FormField
from wtforms import SelectField
from wtforms import FileField
from wtforms.widgets import ListWidget
from wtforms.fields.html5 import EmailField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import TimeField
from wtforms.fields.html5 import DateTimeField
import functions

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')

class LoginForm(Form):
    password = PasswordField('Contraseña: ', [validators.Required(message='El password es requerido.')])

    #def __init__(self, *args, **kwargs):
    #    super(LoginForm, self).__init__(*args, **kwargs)
    #    self.username.choices = functions.creadordelista()

class CreateForm(Form):
    nameuser=StringField('Apellido y nombre: ', [validators.Required(message='El apellido y nombre es requerido.'), validators.length(min=4, max=50, message='Ingrese un apellido y nombre valido.')])
    #lista=RadioField('Lista: ', choices=[('1', 'lista 1'), ('2', 'lista 2')])
    #checkbox=BooleanField('Check: ')

class matchForm(Form):
    #Jugadores

    player01=SelectField('Nombre del jugador 1: ')
    score01=FloatField('Score del jugador 1: ')
    player02=SelectField('Nombre del jugador 1: ')
    score02=FloatField('Score del jugador 1: ')
    player03=SelectField('Nombre del jugador 1: ')
    score03=FloatField('Score del jugador 1: ')
    player04=SelectField('Nombre del jugador 1: ')
    score04=FloatField('Score del jugador 1: ')
    player05=SelectField('Nombre del jugador 1: ')
    score05=FloatField('Score del jugador 1: ')
    player06=SelectField('Nombre del jugador 1: ')
    score06=FloatField('Score del jugador 1: ')
    player07=SelectField('Nombre del jugador 1: ')
    score07=FloatField('Score del jugador 1: ')
    player08=SelectField('Nombre del jugador 1: ')
    score08=FloatField('Score del jugador 1: ')
    player09=SelectField('Nombre del jugador 1: ')
    score09=FloatField('Score del jugador 1: ')
    player10=SelectField('Nombre del jugador 1: ')
    score10=FloatField('Score del jugador 1: ')
    player11=SelectField('Nombre del jugador 1: ')
    score11=FloatField('Score del jugador 1: ')
    player12=SelectField('Nombre del jugador 1: ')
    score12=FloatField('Score del jugador 1: ')
    player13=SelectField('Nombre del jugador 1: ')
    score13=FloatField('Score del jugador 1: ')
    player14=SelectField('Nombre del jugador 1: ')
    score14=FloatField('Score del jugador 1: ')
    player15=SelectField('Nombre del jugador 1: ')
    score15=FloatField('Score del jugador 1: ')
    player16=SelectField('Nombre del jugador 1: ')
    score16=FloatField('Score del jugador 1: ')
    player17=SelectField('Nombre del jugador 1: ')
    score17=FloatField('Score del jugador 1: ')
    player18=SelectField('Nombre del jugador 1: ')
    score18=FloatField('Score del jugador 1: ')
    player19=SelectField('Nombre del jugador 1: ')
    score19=FloatField('Score del jugador 1: ')
    player20=SelectField('Nombre del jugador 1: ')
    score20=FloatField('Score del jugador 1: ')
    player21=SelectField('Nombre del jugador 1: ')
    score21=FloatField('Score del jugador 1: ')
    player22=SelectField('Nombre del jugador 1: ')
    score22=FloatField('Score del jugador 1: ')
    player23=SelectField('Nombre del jugador 1: ')
    score23=FloatField('Score del jugador 1: ')
    player24=SelectField('Nombre del jugador 1: ')
    score24=FloatField('Score del jugador 1: ')
    player25=SelectField('Nombre del jugador 1: ')
    score25=FloatField('Score del jugador 1: ')
    player26=SelectField('Nombre del jugador 1: ')
    score26=FloatField('Score del jugador 1: ')
    player27=SelectField('Nombre del jugador 1: ')
    score27=FloatField('Score del jugador 1: ')
    player28=SelectField('Nombre del jugador 1: ')
    score28=FloatField('Score del jugador 1: ')
    player29=SelectField('Nombre del jugador 1: ')
    score29=FloatField('Score del jugador 1: ')
    player30=SelectField('Nombre del jugador 1: ')
    score30=FloatField('Score del jugador 1: ')
    

    def __init__(self, *args, **kwargs):
        super(matchForm, self).__init__(*args, **kwargs)
        self.player01.choices = functions.listadejugadores()
        self.player02.choices = functions.listadejugadores()
        self.player03.choices = functions.listadejugadores()
        self.player04.choices = functions.listadejugadores()
        self.player05.choices = functions.listadejugadores()
        self.player06.choices = functions.listadejugadores()
        self.player07.choices = functions.listadejugadores()
        self.player08.choices = functions.listadejugadores()
        self.player09.choices = functions.listadejugadores()
        self.player10.choices = functions.listadejugadores()
        self.player11.choices = functions.listadejugadores()
        self.player12.choices = functions.listadejugadores()
        self.player13.choices = functions.listadejugadores()
        self.player14.choices = functions.listadejugadores()
        self.player15.choices = functions.listadejugadores()
        self.player16.choices = functions.listadejugadores()
        self.player17.choices = functions.listadejugadores()
        self.player18.choices = functions.listadejugadores()
        self.player19.choices = functions.listadejugadores()
        self.player20.choices = functions.listadejugadores()
        self.player21.choices = functions.listadejugadores()
        self.player21.choices = functions.listadejugadores()
        self.player22.choices = functions.listadejugadores()
        self.player23.choices = functions.listadejugadores()
        self.player24.choices = functions.listadejugadores()
        self.player25.choices = functions.listadejugadores()
        self.player26.choices = functions.listadejugadores()
        self.player27.choices = functions.listadejugadores()
        self.player28.choices = functions.listadejugadores()
        self.player29.choices = functions.listadejugadores()
        self.player30.choices = functions.listadejugadores()