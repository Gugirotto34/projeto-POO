
class Cliente:
    def __init__(self, nome, idade,cpf,medicamento):
        self.nome=nome
        self.idade=idade
        self.cpf=cpf
        self.medicamento=medicamento
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_cpf(self):
        return self.cpf
    def get_medicamento(self):
        return self.medicamento
    def get_info(self):
        print('nome: {} idade:{} cpf: {} medicamento: {}'.format(self.nome,self.idade,self.cpf,self.medicamento))
    
    def set_nome(self,nome):
        self.nome = nome
    def set_idade(self,idade):
        self.idade = idade
    def set_cpf(self,cpf):
        self.cpf = cpf
    def set_medicamento(self,medicamento):
        selfmedicamento = medicamento
    def set_info(self, nome, idade,cpf,medicamento):
        self.nome=nome
        self.idade=idade
        self.cpf=cpf
        self.medicamento=medicamento
        