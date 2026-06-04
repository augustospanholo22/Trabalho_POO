from Modelos.cliente import Cliente
from Modelos.produtos import Produtos
from Modelos.loja import Loja
from Modelos.pedido import Pedido

try:
    print("======================================")
    print("      SISTEMA DE LOJA VIRTUAL")
    print("======================================\n")

    # Cadastro do cliente
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade: "))
    cpf = input("Digite o CPF: ")

    cliente1 = Cliente(nome, idade, cpf)

    print("\nCliente cadastrado com sucesso!")
    print(cliente1.exibir_detalhes())

    # Loja de roupas
    camiseta = Produtos("Camiseta", 50.00, 10)
    calca = Produtos("Calça Jeans", 120.00, 5)
    tenis = Produtos("Tênis", 200.00, 3)

    # Loja de eletrônicos
    mouse = Produtos("Mouse Gamer", 150.00, 8)
    teclado = Produtos("Teclado Mecânico", 350.00, 4)
    headset = Produtos("Headset", 280.00, 6)

    # Loja de acessórios
    relogio = Produtos("Relógio", 500.00, 2)
    pulseira = Produtos("Pulseira", 80.00, 15)
    oculos = Produtos("Óculos", 250.00, 7)

    loja_roupas = Loja()
    loja_eletronicos = Loja()
    loja_acessorios = Loja()

    # Adicionando produtos
    loja_roupas.adicionar_produto(camiseta)
    loja_roupas.adicionar_produto(calca)
    loja_roupas.adicionar_produto(tenis)

    loja_eletronicos.adicionar_produto(mouse)
    loja_eletronicos.adicionar_produto(teclado)
    loja_eletronicos.adicionar_produto(headset)

    loja_acessorios.adicionar_produto(relogio)
    loja_acessorios.adicionar_produto(pulseira)
    loja_acessorios.adicionar_produto(oculos)

    continuar = True

    while continuar:

        print("\n======================================")
        print("            MENU DE PRODUTOS")
        print("======================================")

        print("\n===== LOJA DE ROUPAS =====")
        print("1 - Camiseta .......... R$50 ")
        print("2 - Calça Jeans ....... R$120")
        print("3 - Tênis ............. R$200")

        print("\n===== LOJA DE ELETRÔNICOS =====")
        print("4 - Mouse Gamer ....... R$150")
        print("5 - Teclado Mecânico .. R$350")
        print("6 - Headset ........... R$280")

        print("\n===== LOJA DE ACESSÓRIOS =====")
        print("7 - Relógio ........... R$500")
        print("8 - Pulseira .......... R$80")
        print("9 - Óculos ............ R$250")

        opcao = int(input("\nEscolha um produto: "))
        quantidade = int(input("Digite a quantidade: "))

        if opcao == 1:
            cliente1.adicionar_ao_carrinho(camiseta, quantidade, loja_roupas)

        elif opcao == 2:
            cliente1.adicionar_ao_carrinho(calca, quantidade, loja_roupas)

        elif opcao == 3:
            cliente1.adicionar_ao_carrinho(tenis, quantidade, loja_roupas)

        elif opcao == 4:
            cliente1.adicionar_ao_carrinho(mouse, quantidade, loja_eletronicos)

        elif opcao == 5:
            cliente1.adicionar_ao_carrinho(teclado, quantidade, loja_eletronicos)

        elif opcao == 6:
            cliente1.adicionar_ao_carrinho(headset, quantidade, loja_eletronicos)

        elif opcao == 7:
            cliente1.adicionar_ao_carrinho(relogio, quantidade, loja_acessorios)

        elif opcao == 8:
            cliente1.adicionar_ao_carrinho(pulseira, quantidade, loja_acessorios)

        elif opcao == 9:
            cliente1.adicionar_ao_carrinho(oculos, quantidade, loja_acessorios)

        else:
            print("Produto inválido.")
            continue

        print("\nProduto adicionado ao carrinho com sucesso!")

        resposta = input("\nDeseja adicionar mais produtos? (s/n): ").lower()

        if resposta != "s":
            continuar = False

    print("\n======================================")
    print("              CARRINHO")
    print("======================================")

    print(cliente1.visualizar_carrinho())

    pedido1 = Pedido(cliente1, cliente1.carrinho)

    print("\n======================================")
    print("          RESUMO DO PEDIDO")
    print("======================================")

    print(pedido1.exibir_resumo())

    print("======================================")
    print("         FINALIZAÇÃO DO PEDIDO")
    print("======================================")

    print(pedido1.finalizar_pedido())

except ValueError as e:
    print(f"\nErro detectado: {e}")