from hamburguer import Hamburguer

class Menu:
    def __init__(self):
        self.hamburgueres = []

    def adicionar_hamburguer(self, hamburguer):
        self.hamburgueres.append(hamburguer)

    def mostrar_menu(self):
        for idx, hamburguer in enumerate(self.hamburgueres, start=1):
            print(f'{idx}. {hamburguer}')
    