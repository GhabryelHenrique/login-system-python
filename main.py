import re
from flask import Flask, Response, request
import mysql.connector
import json

app = Flask(__name__)
con = mysql.connector.connect(
    host='localhost', database='cadastro', user='root', password='1234')

if con.is_connected():
    db_ifo = con.get_server_info()
    print('Conectado ao servidor MYSQL versão ', db_ifo)

    cursor = con.cursor(buffered=True)
    cursor.execute('select database()')


@app.route('/olamundo', methods=["GET"])
def get():
    cursor.execute('select database()'),
    linha = cursor.fetchone(),
    print('Conectado ao banco de dados ', linha)
    return 'Conectado ao banco de dados '


@app.route('/register', methods=["POST"])
def cria_usuario():
    cursor = con.cursor(buffered=True)

    # Insert 3 records
    names = ('zelia', 'silzeliassf@gmail.com', 88894983668, 'ssf2808')
    stmt_insert = "INSERT INTO usuarios (nome, email, cpf, senha) VALUES (%s, %s, %s, %s)"
    cursor.executemany(stmt_insert, (names,))

    # Make sure data is committed to the database
    con.commit()

    cursor.close()
    con.close()
    return 'Sucesso'

app.run()