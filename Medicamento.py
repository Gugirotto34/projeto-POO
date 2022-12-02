
class Medicamento:
    def __init__(self, idM,nome, validade):
        self.idM=idM
        self.nome=nome
        self.validade=validade
    def get_nome(self):
        return self.nome
    def get_validade(self):
        return self.validade
    def get_idM(self):
        return self.idM
    def get_info(self):
        print('id: {} nome: {} validade:{} '.format(self.idM,self.nome,self.validade,))
    
    def set_nome(self,nome):
        self.nome = nome
    def set_validade(self,validade):
        self.validade = validade
    def set_idM(self,idM):
        self.idM = idM
    def set_info(self, nome, validade, idM):
        self.idM=idM
        self.nome=nome
        self.validade=validade
        self.idM=idM
        