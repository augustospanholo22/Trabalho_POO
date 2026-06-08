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

    # Produtos
    camiseta = Produtos("Camiseta", 50.00, 10)
    calca = Produtos("Calça Jeans", 120.00, 5)
    tenis = Produtos("Tênis", 200.00, 3)

    mouse = Produtos("Mouse Gamer", 150.00, 8)
    teclado = Produtos("Teclado Mecânico", 350.00, 4)
    headset = Produtos("Headset", 280.00, 6)

    relogio = Produtos("Relógio", 500.00, 2)
    pulseira = Produtos("Pulseira", 80.00, 15)
    oculos = Produtos("Óculos", 250.00, 7)

    # Criação das lojas
    loja_roupas = Loja()
    loja_eletronicos = Loja()
    loja_acessorios = Loja()

    # Adicionando produtos as lojas
    loja_roupas.adicionar_produto(camiseta)
    loja_roupas.adicionar_produto(calca)
    loja_roupas.adicionar_produto(tenis)

    loja_eletronicos.adicionar_produto(mouse)
    loja_eletronicos.adicionar_produto(teclado)
    loja_eletronicos.adicionar_produto(headset)

    loja_acessorios.adicionar_produto(relogio)
    loja_acessorios.adicionar_produto(pulseira)
    loja_acessorios.adicionar_produto(oculos)

    todas_lojas = [
        ("ROUPAS", loja_roupas),
        ("ELETRÔNICOS", loja_eletronicos),
        ("ACESSÓRIOS", loja_acessorios)
    ]

    continuar = True

    while continuar:

        print("\n======================================")
        print("            MENU DE PRODUTOS")
        print("======================================")

        produtos_menu = []
        contador = 1

        for nome_loja, loja in todas_lojas:

            print(f"\n===== LOJA DE {nome_loja} =====")

            for produto in loja.lista_produtos:
                print(
                    f"{contador} - {produto.nome} | "
                    f"R${produto.preco:.2f} | "
                    f"Estoque: {produto.estoque}"
                )

                produtos_menu.append((produto, loja))
                contador += 1

        opcao = int(input("\nEscolha um produto: "))
        quantidade = int(input("Digite a quantidade: "))

        if 1 <= opcao <= len(produtos_menu):

            produto, loja = produtos_menu[opcao - 1]

            cliente1.adicionar_ao_carrinho(
                produto,
                quantidade,
                loja
            )

            print(f"\n{produto.nome} adicionado ao carrinho!")

        else:
            print("Produto inválido.")
            continue

        resposta = input("\nDeseja adicionar mais produtos? (s/n): ").lower()

        if resposta != "s":
            continuar = False

    print("\n======================================")
    print("              CARRINHO")
    print("======================================")

    print(cliente1.visualizar_carrinho())

    pedido1 = Pedido(cliente1, cliente1.carrinho.copy())

    print("\n======================================")
    print("          RESUMO DO PEDIDO")
    print("======================================")

    print(pedido1.exibir_resumo())

    print("\n======================================")
    print("         FINALIZAÇÃO DO PEDIDO")
    print("======================================")

    print(pedido1.finalizar_pedido())

except ValueError as e:
    print(f"\nErro detectado: {e}")