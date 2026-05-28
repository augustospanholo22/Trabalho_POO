from Modelos.produtos import Produtos

class Loja:
    def __init__(self, lista_produtos=None):
        if lista_produtos is None:
            self.lista_produtos = []
        else:
            self.lista_produtos = lista_produtos

    @property
    def lista_produtos(self):
        return self.__lista_produtos
    
    @lista_produtos.setter
    def lista_produtos(self, nova_lista):
        if not isinstance(nova_lista, list):
            raise TypeError("deve ser uma lista")
        self.__lista_produtos = nova_lista

    def adicionar_produto(self, produto):
        if not isinstance(produto, Produtos):
            raise TypeError("O item adicionado a loja deve ser um produto")
        self.lista_produtos.append(produto)
        


    def listar_produtos(self):
        detalhes = "Produtos disponiveis:\n"
        for p in self.lista_produtos:
            detalhes += f"- {p.nome}: R${p.preco:.2f}\n"
        return detalhes
