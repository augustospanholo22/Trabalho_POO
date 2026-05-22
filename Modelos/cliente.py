from Modelos.pessoas import Pessoas

class Cliente(Pessoas):

    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)

        
    def ExibirNome(self):
        print("O nome do cliente é: ", self.get_nome())