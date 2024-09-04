import sqlite3

class CadastroUsuario:
    def __init__(self, db_name='usuarios.db'):
        self.db_name = db_name
        self._criar_tabela()

    def _criar_tabela(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        ''')
        conn.commit()
        conn.close()

    def adicionar_usuario(self, nome, email):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))
            conn.commit()
            print(f"Usuário {nome} cadastrado com sucesso.")
        except sqlite3.IntegrityError:
            print(f"Usuário com o email {email} já está cadastrado.")
        conn.close()

    def retornar_usuario(self, email):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT nome, email FROM usuarios WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"Nome: {user[0]}, Email: {user[1]}"
        else:
            return "Usuário não encontrado."
