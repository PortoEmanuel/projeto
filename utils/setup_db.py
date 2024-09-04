
import sqlite3

def criar_banco():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    
    # Cria a tabela de usuários
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_banco()
