# ESSE CÓDIGO FOI DESENVOLVIDO PARA NÃO TER VULNERÁBILIDADES, AFINS DE TESTES DE SQL INJECTION

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def hash_password(password):
    # Função para hash da senha usando SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def index():
    if 'username' in session:
        return f'Olá, {session["username"]}! <a href="/logout">Logout</a>'
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        hashed_password = hash_password(password)
        
        # AO USAR MARCADORES '?' EVITA QUE OS VALORES INSERIDOS PELOS USUÁRIOS SEJAM INTERPRETADOS DURANTE A CONSULTA SQL
        query = "SELECT * FROM usuarios WHERE username=? AND password=?"
        c.execute(query, (username, hashed_password))
        user = c.fetchone()
        conn.close()
        if user:
            session['username'] = user[1]
            return redirect(url_for('index'))
        else:
            return 'Login inválido'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)




