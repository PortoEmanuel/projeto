# Sistema de Cadastro de Usuários

Este projeto é um sistema de cadastro de usuários usando Python e SQLite. O sistema permite adicionar, consultar, listar e remover usuários de um banco de dados SQLite.

## Funcionalidades

- **Adicionar Usuário:** Permite adicionar um novo usuário com nome, email, idade (opcional) e bio (opcional).
- **Consultar Usuário:** Permite consultar informações de um usuário com base no email.
- **Listar Usuários:** Mostra uma lista com os nomes de todos os usuários cadastrados.
- **Remover Usuário:** Permite remover um usuário com base no email.

## Requisitos

- Python 3.x
- SQLite (já incluído no Python)

## Estrutura do Projeto

\```
projeto/
├── env/
│   ├── bin/
│   ├── lib/
│   │   └── python3.11/
│   │       └── site-packages/
│   │           ├── _distutils_hack/
│   │           ├── pip/
│   │           ├── pkg_resources/
│   │           ├── setuptools/
│   │           └── wheel/
│   └── pyvenv.cfg
├── play.py
├── README.md
├── usuarios.db
├── utils/
│   ├── __pycache__/
│   ├── setup_db.py
│   ├── usuarios.db
│   └── utilits.py
└── __pycache__/
\```


# Uso
Execute o Script Principal:

sh

python main.py


# Interaja com o Menu:

## O menu principal fornece as seguintes opções:

1. Adicionar usuário: Insira o nome, email, idade (opcional) e bio (opcional) do usuário.
2. Retornar usuário: Consulte informações do usuário com base no email fornecido.
3. Listar todos os usuários: Exibe uma lista com todos os nomes de usuários cadastrados.
4. Remover usuário: Remove um usuário com base no email fornecido.
5. Sair: Encerra o aplicativo.


# Exemplo de Uso
Ao executar o script main.py, você verá o seguinte menu:

markdown

BEM VINDO AO CADASTRO DE USÚARIOS!
Iniciar Aplicativo?? [s,n]: s

Menu:
1. Adicionar usuário
2. Retornar usuário
3. Listar todos os usuários
4. Remover usuário
5. Sair

Escolha uma opção:
Escolha a opção desejada e siga as instruções na tela.

# Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests. Por favor, siga o guia de contribuição para garantir uma colaboração harmoniosa.

### Licença
Este projeto está licenciado sob a MIT License.

