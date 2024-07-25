from sistema_de_vendas import SistemaDeVendas
from cliente import Cliente

def main():
    sistema = SistemaDeVendas()

    # Adicionando alguns hambúrgueres ao menu
    sistema.adicionar_hamburguer_ao_menu("Cheeseburger", 12.50)
    sistema.adicionar_hamburguer_ao_menu("Hamburger", 10.00)
    sistema.adicionar_hamburguer_ao_menu("Bacon Burger", 14.00)
    sistema.adicionar_hamburguer_ao_menu("Veggie Burger", 11.00)

    while True:
        print("\n")
        print("*" * 50)
        print("\n1. Mostrar Menu")
        print("2. Iniciar Pedido")
        print("3. Adicionar Item ao Pedido")
        print("4. Finalizar Pedido")
        print("5. Cadastrar Cliente")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        print("*" * 50)

        if escolha == '1':
            sistema.mostrar_menu()
        elif escolha == '2':
            print("\n**** Você possui cadastro? ****")
            print("1: SIM")
            print("2: NÃO")
            escolha2 = input("Escolha uma opção: ")
            if escolha2 == '1':
                cont = 0
                while True:
                    cont += 1
                    if cont == 4:
                        break
                    cpf = input("Digite o CPF de cadastro: ")
                    if len(cpf) == 11:
                        cliente = sistema.obter_cliente(cpf)
                        if cliente:
                            sistema.iniciar_pedido(cliente)
                            print(f"Novo pedido iniciado para {cliente.nome}.")
                            break
                        else:
                            print("CPF não encontrado.")
                    else:
                        print("**** CPF inválido! ****")
            else:
                print("Cadastro de novo cliente.")
                nome = input("Nome: ")
                while True:
                    cpf = input("CPF: ")
                    if len(cpf) == 11:
                        break
                    else:
                        print("**** CPF inválido! Deve ter 11 dígitos. ****")
                cep = input("CEP: ")
                n_residencial = input("Número Residencial: ")
                endereco = input("Endereço: ")
                telefone = input("Telefone: ")
                novo_cliente = Cliente(nome, cpf, cep, n_residencial, endereco, telefone)
                sistema.adicionar_cliente(novo_cliente)
                sistema.iniciar_pedido(novo_cliente)
                print(f"Novo pedido iniciado para {novo_cliente.nome}.")
        elif escolha == '3':
            indice = int(input("Digite o número do hambúrguer para adicionar ao pedido: "))
            sistema.adicionar_ao_pedido(indice)
        elif escolha == '4':
            sistema.finalizar_pedido()
        elif escolha == '5':
            print("Cadastro de novo cliente.")
            nome = input("Nome: ")
            while True:
                cpf = input("CPF: ")
                if len(cpf) == 11:
                    break
                else:
                    print("**** CPF inválido! Deve ter 11 dígitos. ****")
            cep = input("CEP: ")
            n_residencial = input("Número Residencial: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            novo_cliente = Cliente(nome, cpf, cep, n_residencial, endereco, telefone)
            sistema.adicionar_cliente(novo_cliente)
            print(f"Cliente {novo_cliente.nome} cadastrado com sucesso.")
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
