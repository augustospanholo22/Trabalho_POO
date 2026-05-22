class Produtos:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir_detalhes(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Estoque: {self.estoque}"
    
    def diminuir_estoque(self, quantidade):
        if quantidade > self.estoque:
            raise ValueError("Quantidade solicitada excede o estoque disponível.")
        self.estoque -= quantidade

    @property
    def nome(self):
        return self.__nome 
        
    @nome.setter
    def nome(self, nome):
        if not nome.strip():
            raise ValueError("O nome do produto não pode estar vazio.")
        self.__nome = nome  

    @property
    def preco(self):
        return self.__preco
        
    @preco.setter
    def preco(self, preco):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.__preco = preco

    @property
    def estoque(self):
        return self.__estoque
        
    @estoque.setter
    def estoque(self, estoque): 
        if estoque < 0:
            raise ValueError("O estoque não pode ser negativo.")
        self.__estoque = estoque