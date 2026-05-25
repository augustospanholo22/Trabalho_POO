from Modelos.cliente import Cliente
from Modelos.pessoas import Pessoas
from Modelos.produtos import Produtos
#from Modelos.loja import Loja
from Modelos.pedido import Pedido



produto1 = Produtos("Camiseta", 50.0, 10)
produto2 = Produtos("Calça Jeans", 120.0, 5)
produto3 = Produtos("Tênis", 200.0, 3)



cliente1 = Cliente("João", 30, "123.456.789-00", [])

cliente1.adicionar_ao_carrinho(produto1, 2)
cliente1.adicionar_ao_carrinho(produto2, 1)
cliente1.adicionar_ao_carrinho(produto3, 3)



pedido1 = Pedido(cliente1, cliente1.carrinho)
print(pedido1.exibir_resumo())
print(pedido1.finalizar_pedido())

print(produto1.exibir_detalhes_produto())