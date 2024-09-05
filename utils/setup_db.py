import sqlite3
import os

def criar_banco():
    db_name = 'usuarios.db'
    if os.path.exists(db_name):
        os.remove(db_name)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Cria a tabela de usuários com os novos campos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        idade INTEGER,
        bio TEXT
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_banco()
