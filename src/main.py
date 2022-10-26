from flask import Flask, render_template, request, make_response, session, redirect, url_for, flash, jsonify
from flask_wtf import CSRFProtect
import sqlite3
from gekko import GEKKO

import forms
import functions

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)

### FUNCIÓN DE CHEQUEO PREVIO AL INGRESO DE CADA PÁGINA ###

@app.before_request
def before_request():
    if 'username' in session:
        username = session['username']
    else:
        pass
    if 'username' in session and username != 'Administrador' and request.endpoint in ['create', 'editplayer', 'delplayer', 'databasemanager', 'match']:
        return redirect(url_for('ranking'))
    if 'username' not in session and request.endpoint in ['create', 'editplayer', 'delplayer', 'databasemanager', 'match']:
        return redirect(url_for('ranking'))

### BASE DE DATOS ###

@app.route('/databasemanager')
def databasemanager():
    basededatos = sqlite3.connect('src/Basededatos')
    cursor = basededatos.cursor()
    cursor.execute('SELECT * FROM JUGADORES')
    jugadoresdata= cursor.fetchall()
    return render_template('databasemanager.html', jugadores=jugadoresdata, title='Administrador de base de datos') 

### BASE DE DATOS ###

@app.route('/')
def ranking():
    basededatos = sqlite3.connect('src/Basededatos')
    cursor = basededatos.cursor()
    cursor.execute('SELECT * FROM JUGADORES')
    jugadoresdata= cursor.fetchall()
    return render_template('ranking.html', jugadores=jugadoresdata, title='ranking')  

### FUNCIÓN PARA CREAR JUGADORES ###

@app.route('/create', methods=['GET', 'POST'])
def create():
    create_form = forms.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():
        perfil = (create_form.nameuser.data, 0, 0)
        functions.creadordeperfil(perfil)
    return render_template('create.html', title='Crear jugador', form=create_form)

### FUNCIÓN PARA EDITAR PERFILES ESTATICOS ###

@app.route('/editplayer/<string:ID>', methods=['GET', 'POST'])
def editperfilest(ID):
    basededatos = sqlite3.connect('src/Basededatos')
    cursor = basededatos.cursor()
    cursor.execute('SELECT * FROM JUGADORES WHERE ID=?', [ID])
    defaultvalue=cursor.fetchall()[0][1]
    print(defaultvalue)
    create_form = forms.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():
        datos=[create_form.nameuser.data, ID]
        functions.actualizarplayer(datos)
        return redirect(url_for('databasemanager'))
    return render_template('create.html', title='Actualizar jugador', form=create_form, username=session['username'], value=defaultvalue)
    
### FUNCIÓN PARA ELIMINAR JUGADORES ###

@app.route('/delplayer/<string:ID>')
def deleleteplayer(ID):
    basededatos = sqlite3.connect('src/Basededatos')
    cursor = basededatos.cursor()
    cursor.execute('SELECT NOMBRE FROM JUGADORES WHERE ID=?', [ID])
    NombreApellido=cursor.fetchone()[0]
    cursor.execute('DELETE FROM JUGADORES WHERE ID=?', [ID])
    basededatos.commit()
    message= '{} ha sido eliminado satisfactoriamente.'.format(NombreApellido)
    flash (message)
    return redirect(url_for('home'))

### FUNCIÓN PARA CARGAR PARTIDOS ###

@app.route('/match', methods=['GET', 'POST'])
def match():
    match_form = forms.matchForm(request.form)
    if request.method == 'POST':
        functions.match(match_form)
        success_message = 'El partido ha sido cargado !'
        flash(success_message)
    return render_template('match.html', title='Cargador de partidos', form=match_form)

### FUNCIÓN PARA ARMAR LOS EQUIPOS ###

@app.route('/team', methods=['GET', 'POST'])
def team():
    match_form = forms.matchForm(request.form)
    if request.method == 'POST':
        functions.team(match_form)
    return render_template('team.html', title='Armador de equipos', form=match_form)

### FUNCIÓN PARA LOGUEARSE ###

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        if str(login_form.password.data)=="pikachu123":
            success_message = 'Bienvenido ADMINISTRADOR !'
            flash(success_message)
            session['username'] = 'Administrador'
            return redirect(url_for('databasemanager'))
        else:
            error_message = 'Ingrese la clave de administrador.'
            flash(error_message)
    return render_template('login.html', title='Ingrese su usuario', form=login_form)

### FUNCIÓN PARA DESLOGUEARSE ###

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('home'))
    
### FUNCIÓN PARA CORRER LA APLICACIÓN

if __name__ == '__main__':
    app.config['TEMPLATES AUTO_RELOAD'] = True
    app.run(debug=True, port=8000)