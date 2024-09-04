# main.py
from utils.utilits import CadastroUsuario

def main():
    print('BEM VINDO AO CADASTRO DE USÚARIOS!')
    opcao = input('Iniciar Aplicativo?? [s,n]: ')
    
    if opcao == 's':
        cadastro = CadastroUsuario()
        
        while True:
            print("\nMenu:")
            print("1. Adicionar usuário")
            print("2. Retornar usuário")
            print("3. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                nome = input("Digite o nome do usuário: ")
                email = input("Digite o email do usuário: ")
                cadastro.adicionar_usuario(nome, email)
            elif escolha == '2':
                email = input("Digite o email do usuário para consulta: ")
                print(cadastro.retornar_usuario(email))
            elif escolha == '3':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Saída do programa.")

if __name__ == "__main__":
    main()
