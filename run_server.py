# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from flask import Flask, render_template, request, redirect, url_for, session
import re
import sqlite3
import os
import db.db


# Création de l'application Flask
SECRET_MESSAGE = "Wagen_zeit" 
app = Flask(__name__)

# Mise en place du système d'authentification

@app.route("/")
@app.route('/login', methods = ['GET', 'POST'])
def login(): # Connexion avec un compte existant
    message = ''
    if request.method == 'POST' and 'userEmail' in request.form and 'password' in request.form :
        # Récupération des données du formulaire
        email = request.form['userEmail']
        password = request.form['password']

        # Vérification des identifiants remplis dans le formulaire
        conn = sqlite3.connect('db/users.sql')
        cursor = conn.cursor()
        req = "SELECT * FROM user WHERE email = '" + email + "' AND password = '" + password + "'"
        cursor.execute(req)
        user = cursor.fetchone()

        if user  :
            return render_template('user.html', userName = user[1], message_secret = SECRET_MESSAGE )
        else :
            message = "Informations don't match !"

    return render_template('login.html', loginmesage = message)

@app.route('/logout') 
def logout(): #Déconnexion d'un compte utilisateur

    return render_template('login.html', registermesage="You're successfully logged-out")


@app.route('/register', methods = ['GET', 'POST'])
def register(): #Création d'un nouveau compte utilisateur
    deniedmessage = ''
    grantedmessage = ''

    if request.method == 'POST' and 'userName' in request.form and 'password' in request.form and 'useremail' in request.form :
        # Récupération des données du formulaire
        userName = request.form['userName']
        password = request.form['password']
        email = request.form['useremail']

        conn = sqlite3.connect('db/users.sql')
        cursor = conn.cursor()
        req = "SELECT * FROM user WHERE email = '" + email + "'"
        cursor.execute(req)
        account = cursor.fetchone()

        if account :
            deniedmessage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email) :
            deniedmesage = 'Invalid email address !'
        elif not userName or not email or not password :
            deniedmessage = 'Please, fill out the form'
        else :
            req = "INSERT INTO user (userID, name, email, password) VALUES (23, '" + userName + "','" + email + "','" + password + "')"
            cursor.execute(req)
            conn.commit()

            grantedmessage = 'Your account is created. Now login !'
    else :
        deniedmessage = 'Please, fill out the register form'
    
    return render_template('login.html', loginmesage =deniedmessage , registermesage = grantedmessage )




def get_secret_message():
    return  SECRET_MESSAGE 


if __name__ == "__main__":
    # HTTP version
    # app.run(debug=True, host="0.0.0.0", port=8081)

    # HTTPS version
    # Chemin vers les fichiers du certificat SSL
    context = ("resources/server-public-key.pem", "resources/server-private-key.pem")

    # Lancement de l'application
    app.run(debug=True, ssl_context=context, port=8081)


