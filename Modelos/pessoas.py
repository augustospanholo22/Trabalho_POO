class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    @property
    def nome(self):
        return self.__nome      
    @nome.setter
    def nome(self, nome):
        if not nome.strip():
            raise ValueError("O nome não pode estar vazio.")
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf  
    @cpf.setter
    def cpf(self, cpf):
        if not cpf.strip():
            raise ValueError("O CPF não pode estar vazio.")
        self.__cpf = cpf
        
    
    def exibir_detalhes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}"
    
