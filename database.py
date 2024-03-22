import sqlite3
import hashlib

# Conexão com o banco de dados
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Criação da tabela de usuários
c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT
            )''')

# Insere algumas contas de exemplo (senhas em texto simples para demonstração)
contas = [
    ('user1', '123'),
    ('user2', '345'),
    ('user3', '456')
]

for conta in contas:
    username, password = conta
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, hashed_password))

# Commit e fechamento da conexão
conn.commit()
conn.close()
