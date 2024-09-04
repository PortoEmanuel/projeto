
### A estrutura do projeto é a seguinte
project-root/
│
├── env/
│   ├── play.py            # Script principal para interagir com a aplicação
│   ├── usuarios.db        # Banco de dados SQLite (gerado automaticamente)
│
└── utils/
    ├── __pycache__/       # Diretório de cache de compilação Python
    ├── setup_db.py        # Script para configurar o banco de dados
    ├── usuarios.db        # Banco de dados SQLite (gerado automaticamente)
    └── utilits.py         # Contém a classe CadastroUsuario com métodos para manipulação de dados

### Requisitos
Python 3.x: O projeto foi desenvolvido e testado com Python 3.x. Certifique-se de ter uma versão compatível instalada.

### crie um ambiente virtual 
python -m venv env
source env/bin/activate

## Execute o script de configuração para criar a tabela usuarios:

### bash
python utils/setup_db.py


