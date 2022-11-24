
class Medicamento:
    def __init__(self, nome, validade, doenca):
        self.nome=nome
        self.validade=validade
        self.doenca=doenca
    def get_nome(self):
        return self.nome
    def get_validade(self):
        return self.validade
    def get_doenca(self):
        return self.doenca
    def get_info(self):
        print('nome: {} validade:{} Sintomas que esse remedio cura: {} '.format(self.nome,self.validade,self.doenca))
    
    def set_nome(self,nome):
        self.nome = nome
    def set_idade(self,validade):
        self.validade = validade
    def set_cpf(self,doenca):
        self.doenca = doenca
    def set_info(self, nome, validade, doenca):
        self.nome=nome
        self.validade=validade
        self.doenca=doenca
        