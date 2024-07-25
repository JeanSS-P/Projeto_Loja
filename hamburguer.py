class Hamburguer:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.cliente = {}

    def __str__(self):
        return f'{self.nome} - R${self.preco:.2f}'
