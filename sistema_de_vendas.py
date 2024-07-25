from menu import Menu
from pedido import Pedido
from cliente import Cliente
from hamburguer import Hamburguer

class SistemaDeVendas:
    def __init__(self):
        self.menu = Menu()
        self.pedido_atual = None
        self.clientes = {}

    def adicionar_cliente(self, cliente):
        self.clientes[cliente.cpf] = cliente

    def obter_cliente(self, cpf):
        return self.clientes.get(cpf, None)

    def iniciar_pedido(self, cliente):
        self.pedido_atual = Pedido(cliente)

    def adicionar_hamburguer_ao_menu(self, nome, preco):
        hamburguer = Hamburguer(nome, preco)
        self.menu.adicionar_hamburguer(hamburguer)

    def mostrar_menu(self):
        self.menu.mostrar_menu()

    def adicionar_ao_pedido(self, indice):
        if self.pedido_atual is None:
            print("Por favor, inicie um novo pedido primeiro.")
            return
        try:
            hamburguer = self.menu.hamburgueres[indice - 1]
            self.pedido_atual.adicionar_item(hamburguer)
        except IndexError:
            print("Hambúrguer não encontrado no menu.")

    def finalizar_pedido(self):
        if self.pedido_atual:
            self.pedido_atual.mostrar_pedido()
            self.pedido_atual = None
        else:
            print("Nenhum pedido em andamento.")
