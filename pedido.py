from hamburguer import Hamburguer

class Pedido:
    def __init__(self, cliente) -> None:
        self.itens = []
        self.total = 0.0
        self.cliente = cliente

    def adicionar_item(self, hamburguer):
        self.itens.append(hamburguer)
        self.total += hamburguer.preco

    def mostrar_pedido(self):
        print(f"Pedido de {self.cliente.nome}:")
        for item in self.itens:
            print(f'- {item}')
        print(f'Total: R${self.total:.2f}')



    