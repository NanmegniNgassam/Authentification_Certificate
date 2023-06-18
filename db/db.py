import sqlite3
import os


if(os.path.exists('db/users.sql')):
    print('La base de données existe déjà')
    #Connexion à une base de données
    conn = sqlite3.connect('db/users.sql')
    cursor = conn.cursor()

    req = 'SELECT * FROM user'
    cursor.execute(req)
    result = cursor.fetchall()

    print(result)

else:
    #Connexion à une base de données
    conn = sqlite3.connect('db/users.sql')
    cursor = conn.cursor()

    #Création d'une table
    request = "CREATE TABLE user(userID INT(4), name VARCHAR(50) NOT NULL, email VARCHAR(100) NOT NULL, password varchar(100) NOT NULL);"
    cursor.execute(request)

    #Chargement de la table
    req = "INSERT INTO user (userID, name, email, password) VALUES (1, 'NGASSAM', 'blk@gmail.com', 'azerty');"
    cursor.execute(req)

    #synchronisation du programme avec la base
    conn.commit()

