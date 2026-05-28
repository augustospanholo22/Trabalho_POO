from Modelos.cliente import Cliente

class Pedido:
    def __init__(self, cliente, produtos):
        self.cliente = cliente
        self.produtos = produtos

    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise ValueError("O cliente deve ser uma instância da classe Cliente.")
        self.__cliente = cliente

    @property
    def produtos(self):
        return self.__produtos
    @produtos.setter
    def produtos(self, produtos):
        if not isinstance(produtos, list):
            raise ValueError("Os produtos devem ser uma lista de instâncias da classe Produtos.")
        self.__produtos = produtos

    def calcular_valor_total(self):
        total = 0
        for p, quantidade in self.produtos:
            total += p.preco * quantidade
        return total


    def exibir_resumo(self):
        detalhes = f"Cliente: {self.cliente.nome}\nProdutos:\n"
        for p, quantidade in self.produtos:
            detalhes += f"- {p.nome} (x{quantidade}): R$ {p.preco:.2f}\n"
        detalhes += f"Valor Total: R$ {self.calcular_valor_total():.2f}\n"
        return detalhes
    
    def finalizar_pedido(self):
        if not self.produtos:
            raise ValueError("O pedido não pode ser finalizado sem produtos.")
        return f"Pedido finalizado para {self.cliente.nome}.\nTotal: R$ {self.calcular_valor_total():.2f}"
    

    

    