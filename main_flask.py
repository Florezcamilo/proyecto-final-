from flask import Flask, request, redirect, url_for, render_template, flash, session
import flask
import sys
from flask import json
from getusers import *
import re

app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.secret_key = 'llave'
indice_user = 0


@app.route('/', methods=['GET', 'POST'])
def login():
    """
    """
    global indice_user
    error = None
    if request.method == 'POST':
        if request.form['uno'] == "ingresar":
            if request.form['username'] != "" and request.form['pswd'] != "":
                user_registrados=[]
                while indice_user < len(users) :
                    if request.form['username'] == users[indice_user][0]:
                        user_registrados.append(request.form['username'])
                        break
                    indice_user+=1                
                if request.form['username'] in user_registrados:
                    i=0
                    while i < len(users):
                        if request.form['pswd'] == users[indice_user][1]:
                            if users[indice_user][3] == 'admin' :
                                return redirect(url_for('holaadmin'))
                            if users[indice_user][3] == 'user' :
                                return redirect(url_for('holauser'))
                        i+=1
                else :
                    flash('Usuario no registrado.')
                    
    return render_template('login.html', error=error)

@app.route('/admin', methods = ["GET","POST"])
def holaadmin():
    """
    """
    if request.method == 'POST':
        return redirect(url_for('registro'))
        
    return render_template('pag_admin.html')

@app.route('/username', methods = ["GET","POST"])
def holauser():
    """
    """
    username = users[indice_user][0]
    if request.method == 'POST':
        if request.form['boton'] == "jugar":
            return redirect(url_for('grado'))
    return render_template('pag_user.html', username = users[indice_user][0])


@app.route('/grado', methods = ["GET","POST"])
def grado():
    """
    """
    grade  = int(users[indice_user][2])
    if request.method == 'POST' :
        
        if request.form['boton3'] == "iniciar curso":
            if grade == 0 :
                return render_template('grado_0.html')
            if grade == 1:
                return render_template('grado_1.html')
            if grade == 2:
                return render_template('grado_2.html')
            if grade == 3 :
                return render_template('grado_3.html')
            if grade == 4 :
                return render_template('grado_4.html')
            if grade == 5 :
                return render_template('grado_5.html')
            if grade == 6 :
                return render_template('grado_6.html')
            if grade == 7 :
                return render_template('grado_7.html')
            if grade == 8 :
                return render_template('grado_8.html')
            if grade == 9 :
                return render_template('grado_final.html')
            
        if request.form['boton3'] == "regresar" :
            return redirect(url_for('holauser'))
    return render_template('grados.html', grade = int(users[indice_user][2]))


@app.route('/registro', methods = ["GET","POST"])
def registro():
    """
    """
    if request.method == 'POST':
        if request.form['username'] !="" and request.form['pswd'] !="":
            match=re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)", request.form['username'])
            if match:
                i=0
                user_exist=[]
                while i<len(users):
                    if request.form['username'] in users[i]:
                        user_exist.append(request.form['username'])
                        break
                    i+=1
                if request.form['username'] in user_exist:
                    flash('El usuario que intenta registrar ya esta en el sistema, intente iniciar sesion.')
                else :
                    if request.form['rol'] == "user" or request.form['rol'] == "admin":
                        file=open('users.txt','a')
                        file.write('\n')
                        file.write(request.form['username'])
                        file.write(',')
                        file.write(request.form['pswd'])
                        file.write(',0')
                        file.write(',')
                        file.write(request.form['rol'])
                        file.close()
                        flash('Registro exitoso')
                    else:
                        flash('El rol unicamente puede ser User o Admin')
            else :
                flash('Email invalido, recuerda utilizar la forma "example@algo.com".')
    return render_template('registro.html')


@app.route('/felicidades', methods = ["GET","POST"])
def felicidades():
    """
    """
    if request.method == 'POST':
        if request.form['boton'] == "regresar":
            grade = int(users[indice_user][2])
            new_grade = grade + 1
            file=open('users.txt','a')
            file.write('\n')
            file.write(users[indice_user][0])
            file.write(',')
            file.write(users[indice_user][1])
            file.write(',')
            file.write(str(new_grade))
            file.write(',')
            file.write(users[indice_user][3])
            file.close()
            return redirect(url_for('holauser'))
    return render_template('felicidades.html', grade = str(users[indice_user][2]))


@app.route('/fracaso', methods = ["GET","POST"])
def fracaso():
    """
    """
    grade = int(users[indice_user][2])
    if request.method == 'POST':
        if request.form['boton'] == "repetir":
            if grade == 0:
                return redirect(url_for('grado_0'))
            if grade == 1:
                return render_template('grado_1.html')
            if grade == 2:
                return render_template('grado_2.html')
            if grade == 3 :
                return render_template('grado_3.html')
            if grade == 4 :
                return render_template('grado_4.html')
            if grade == 5 :
                return render_template('grado_5.html')
            if grade == 6 :
                return render_template('grado_6.html')
            if grade == 7 :
                return render_template('grado_7.html')
            if grade == 8 :
                return render_template('grado_8.html')
            if grade == 9 :
                return render_template('grado_final.html')
            
    return render_template('fracaso.html', grade = str(users[indice_user][2]))
if __name__ == '__main__':
    app.run(debug=True)

