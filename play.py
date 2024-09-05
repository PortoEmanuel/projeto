# main.py
from utils.utilits import CadastroUsuario

def main():
    print('BEM VINDO AO CADASTRO DE USÚARIOS!')
    opcao = input('Iniciar Aplicativo?? [s,n]: ')
    
    if opcao.lower() == 's':
        cadastro = CadastroUsuario()
        
        while True:
            print("\nMenu:")
            print("1. Adicionar usuário")
            print("2. Retornar usuário")
            print("3. Listar todos os usuários")
            print("4. Remover usuário")
            print("5. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                nome = input("Digite o nome do usuário: ")
                email = input("Digite o email do usuário: ")
                idade = input("Digite a idade do usuário (opcional): ")
                bio = input("Digite a bio do usuário (opcional): ")
                
                idade = int(idade) if idade else None
                cadastro.adicionar_usuario(nome, email, idade, bio)
            elif escolha == '2':
                email = input("Digite o email do usuário para consulta: ")
                print(cadastro.retornar_usuario(email))
            elif escolha == '3':
                usuarios = cadastro.listar_usuarios()
                if usuarios:
                    print("\nLista de Usuários:")
                    for usuario in usuarios:
                        print(usuario)
                else:
                    print("Nenhum usuário encontrado.")
            elif escolha == '4':
                email = input("Digite o email do usuário que deseja remover: ")
                cadastro.remover_usuario(email)
            elif escolha == '5':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Saída do programa.")

if __name__ == "__main__":
    main()
