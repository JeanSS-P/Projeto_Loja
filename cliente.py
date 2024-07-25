class Cliente:
    def __init__(self, nome,cpf, cep,n_residencial, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep
        self.numero = n_residencial
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self) -> str:
        return (f'Nome: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}, '
                f'Número: {self.n_residencial}, CEP: {self.cep}, Telefone: {self.telefone}')



         