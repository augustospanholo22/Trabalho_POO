from typing import override

from Modelos.produtos import Produtos
from Modelos.pessoas import Pessoas
from Modelos.loja import Loja

class Cliente(Pessoas):
    def __init__(self, nome, idade, cpf, carrinho=None):
        super().__init__(nome, idade, cpf)
        if carrinho is None:
            self.carrinho = []
        else:
            self.carrinho = carrinho

    @property
    def carrinho(self):
        return self.__carrinho
    @carrinho.setter
    def carrinho(self, carrinho):
        if not isinstance(carrinho, list):
            raise ValueError("O carrinho deve ser uma lista de produtos.")
        self.__carrinho = carrinho

    @override
    def exibir_dados(self):
        detalhes_pessoa = super().exibir_detalhes()
        return f"{detalhes_pessoa}, Carrinho: {len(self.carrinho)} itens"

    def adicionar_ao_carrinho(self, produto, quantidade, loja):
        if not isinstance (loja, Loja):
            raise ValueError("O item adicionado ao carrinho deve ser uma instância da classe Loja.")
        if not isinstance(produto, Produtos):
            raise ValueError("O item adicionado ao carrinho deve ser uma instância da classe Produtos.")
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if produto.estoque < quantidade:
            raise ValueError("Quantidade solicitada excede o estoque disponível.")
        
        if not produto in loja.lista_produtos:
            raise ValueError("Produto indisponível na Loja")
        self.carrinho.append((produto, quantidade))
        produto.diminuir_estoque(quantidade)

    def visualizar_carrinho(self):
        if not self.carrinho:
            return "O carrinho está vazio."
        detalhes = "Carrinho:\n"
        for p, quantidade in self.carrinho:
            detalhes += f"- {p.nome} (x{quantidade}): R$ {p.preco:.2f}\n"
        return detalhes
    
