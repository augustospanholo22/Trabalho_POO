from Modelos.cliente import Cliente
from Modelos.pessoas import Pessoas


cliente1 = Cliente("Augusto", 20, "123.456.789-00")
pessoa1 = Pessoas("Maria", 30, "987.654.321-00")

print(pessoa1.get_nome())
cliente1.ExibirNome()