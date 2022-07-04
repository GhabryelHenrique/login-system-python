from flask import Flask, Response, request, session, make_response
import mysql.connector

app = Flask(__name__)
app.secret_key = "super secret key"
con = mysql.connector.connect(
    host='localhost', database='cadastro', user='root', password='1234')

if con.is_connected():
    db_ifo = con.get_server_info()
    print('Conectado ao servidor MYSQL versão ', db_ifo)

    cursor = con.cursor(buffered=True)
    cursor.execute('select database()')


@app.route('/register', methods=["POST"])
def cria_usuario():
    nome = request.json.get('nome')
    email = request.json.get('email')
    cpf = request.json.get('cpf')
    senha = request.json.get('senha')

    cursor = con.cursor(buffered=True)

    names = (nome, email, cpf, senha)
    try:
        stmt_insert = "INSERT INTO users (nome, email, cpf, senha) VALUES (%s, %s, %s, %s)"
        cursor.executemany(stmt_insert, (names,))

        # Make sure data is committed to the database
        con.commit()

        cursor.close()
        return 'Sucesso'

    except:
        return 'Informe todas as informações', 404


@app.route('/login', methods=["GET","POST"])
def login():
    email = request.json.get('email')
    senha = request.json.get('password')
    cursor = con.cursor(buffered=True)
    if request.method == 'POST':
        try:
            cursor.execute('SELECT * FROM users WHERE email=%s AND senha=%s', (email, senha))
            record = cursor.fetchone()
            print(record)
            session['loggedin'] = True
            session['username'] = record[1]
            return make_response(email)

        except:
            return 'Email/Senha Incorreta, Tente Novamente', 404


app.run()
