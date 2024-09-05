import sqlite3 # Importa a biblioteca SQLite para manipulação de banco de dados.

class CadastroUsuario: #  Define a classe CadastroUsuario.
    def __init__(self, db_name='usuarios.db'): #  O método construtor que inicializa a classe.
        self.db_name = db_name # Define o nome do banco de dados (padrão é 'usuarios.db').
        self._criar_tabela()  # Chama o método privado _criar_tabela para criar a tabela

    def _criar_tabela(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
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

    def adicionar_usuario(self, nome, email, idade=None, bio=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        try:
            cursor.execute('''
            INSERT INTO usuarios (nome, email, idade, bio) VALUES (?, ?, ?, ?)
            ''', (nome, email, idade, bio))
            conn.commit()
            print(f"Usuário {nome} cadastrado com sucesso.")
        except sqlite3.IntegrityError:
            print(f"Usuário com o email {email} já está cadastrado.")
        conn.close()

    def retornar_usuario(self, email):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT nome, email, idade, bio FROM usuarios WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"Nome: {user[0]}, Email: {user[1]}, Idade: {user[2]}, Bio: {user[3]}"
        else:
            return "Usuário não encontrado."
        
    def listar_usuarios(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT nome FROM usuarios')
        usuarios = cursor.fetchall()
        conn.close()

        if usuarios:
            return [usuario[0] for usuario in usuarios]
        else:
            return []
        
    def remover_usuario(self, email):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM usuarios WHERE email = ?', (email,))
        conn.commit()
        conn.close()

        if cursor.rowcount > 0:
            print(f"Usuário com o email {email} foi removido com sucesso.")
        else:
            print(f"Usuário com o email {email} não encontrado.")
