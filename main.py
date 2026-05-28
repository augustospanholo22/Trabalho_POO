from Modelos.cliente import Cliente
from Modelos.pessoas import Pessoas
from Modelos.produtos import Produtos
from Modelos.loja import Loja
from Modelos.pedido import Pedido


try:
    cliente1 = Cliente("João", 30, "123.456.789-00")

    produto1 = Produtos("Camiseta", 50.00, 10)
    produto2 = Produtos("Calça Jeans", 120.00, 5)
    produto3 = Produtos("Tênis", 200.00, 3)
    produto4 = Produtos("Brinco", 300.00, 4)
    produto5 = Produtos("Pulseira", 150.00, 8)


    lojaRoupas = Loja()
    lojaRoupas.adicionar_produto(produto1)
    lojaRoupas.adicionar_produto(produto2)
    lojaRoupas.adicionar_produto(produto3)
    print(lojaRoupas.listar_produtos())

    lojaJoias = Loja()
    lojaJoias.adicionar_produto(produto4)
    lojaJoias.adicionar_produto(produto5)
    print(lojaJoias.listar_produtos())



    cliente1.adicionar_ao_carrinho(produto1, 2, lojaRoupas)
    cliente1.adicionar_ao_carrinho(produto2, 1, lojaRoupas)
    cliente1.adicionar_ao_carrinho(produto5, 3, lojaJoias)



    pedido1 = Pedido(cliente1, cliente1.carrinho)
    print(pedido1.exibir_resumo())
    print(pedido1.finalizar_pedido())

    print(produto1.exibir_detalhes_produto())
except ValueError as e:
    print(f"Erro detectado: {e}")