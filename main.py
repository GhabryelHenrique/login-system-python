from flask import Flask, Response, request
import mysql.connector
import json

app = Flask(__name__)
con = mysql.connector.connect(
    host='localhost', database='cadastro', user='root', password='xxxx')

if con.is_connected():
    db_ifo = con.get_server_info()
    print('Conectado ao servidor MYSQL versão ', db_ifo)

    cursor = con.cursor(buffered=True)
    cursor.execute('select database()')

@app.route('/register', methods=["POST"])
def cria_usuario():
    nome = request.body.get('usuario')
    email = request.body.get('email@email.com')
    cpf = request.body.get(123)
    senha = request.body.get('123456')

    cursor = con.cursor(buffered=True)

    # Insert 3 records
    names = (nome, email, cpf, senha)
    stmt_insert = "INSERT INTO usuarios (nome, email, cpf, senha) VALUES (%s, %s, %s, %s)"
    cursor.executemany(stmt_insert, (names,))

    # Make sure data is committed to the database
    con.commit()

    cursor.close()
    con.close()
    return 'Sucesso'

app.run()